import os
import random
import shutil


def to_sub(dir):
    return dir + '/images', dir + '/labels'


def move_random_files(src_folder, dst_folder_T, dst_folder_V, percentage=0.1):
    src_img_file, src_text_file = to_sub(src_folder)
    dst_img_file_T, dst_text_file_T = to_sub(dst_folder_T)
    dst_img_file_V, dst_text_file_V = to_sub(dst_folder_V)
    imgs1 = [f for f in os.listdir(src_img_file) if (f.endswith('.jpg') or f.endswith('.png'))]
    # texts = [f for f in os.listdir(src_text_file) if f.endswith('.txt')]
    num_files = len(imgs1)
    num_to_move = round(num_files * percentage)
    print(num_to_move)
    imgs_to_dst1 = random.sample(imgs1, num_to_move)
    text_to_dst1 = [os.path.splitext(file)[0] + '.txt' for file in imgs_to_dst1]
    print(imgs_to_dst1)
    print(text_to_dst1)
    for file in imgs_to_dst1:
        shutil.move(os.path.join(src_img_file, file), os.path.join(dst_img_file_T, file))
    for file in text_to_dst1:
        shutil.move(os.path.join(src_text_file, file), os.path.join(dst_text_file_T, file))
    print("complete A")

    imgs2 = [f for f in os.listdir(src_img_file) if (f.endswith('.jpg') or f.endswith('.png'))]
    imgs_to_dst2 = random.sample(imgs2, num_to_move)
    text_to_dst2 = [os.path.splitext(file)[0] + '.txt' for file in imgs_to_dst2]
    print(imgs_to_dst2)
    print(text_to_dst2)
    for file in imgs_to_dst2:
        shutil.move(os.path.join(src_img_file, file), os.path.join(dst_img_file_V, file))
    for file in text_to_dst2:
        shutil.move(os.path.join(src_text_file, file), os.path.join(dst_text_file_V, file))
    print("complete B")

    for i in imgs_to_dst1:
        if i in imgs_to_dst2:
            print("error occurred in ", i)


folder = './'

cate = ['0_bellpepper_fresh/', '1_bellpepper_rotten/', '2_bitterground_fresh/', '3_bitterground_rotten/', '4_capsicum_fresh/', '5_capsicum_rotten/', '6_carrot_fresh/', '7_carrot_rotten/', '8_cucumber_fresh/', '9_cucumber_rotten/', '10_okra_fresh/', '11_okra_rotten/', '12_potato_fresh/', '13_potato_rotten/']
# cate = ['11_okra_rotten/']
tofile = ['train', 'test', 'valid']

for i, item in enumerate(cate):
    print(i, item)
    src_folder = folder + item + tofile[0]
    dst_folder_test = folder + item + tofile[1]
    dst_folder_valid = folder + item + tofile[2]
    os.makedirs(dst_folder_test, exist_ok=True)
    os.makedirs(dst_folder_valid, exist_ok=True)
    move_random_files(src_folder, dst_folder_test, dst_folder_valid)

