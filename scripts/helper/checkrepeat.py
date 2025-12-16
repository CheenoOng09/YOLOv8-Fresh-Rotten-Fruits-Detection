import os

def get_file_names_without_extension(folder):
    # 取得資料夾內所有檔案名稱，並去掉副檔名
    return {os.path.splitext(f)[0] for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))}

def find_unique_files(folder1, folder2):
    # 取得兩個資料夾內去掉副檔名的檔案名稱集合
    files_in_folder1 = get_file_names_without_extension(folder1)
    files_in_folder2 = get_file_names_without_extension(folder2)

    # 找出只存在於 folder1 而不存在於 folder2 的檔案
    unique_in_folder1 = files_in_folder1 - files_in_folder2
    # 找出只存在於 folder2 而不存在於 folder1 的檔案
    unique_in_folder2 = files_in_folder2 - files_in_folder1

    return unique_in_folder1, unique_in_folder2

folder = './'
cate = ['0_bellpepper_fresh/', '1_bellpepper_rotten/', '2_bitterground_fresh/', '3_bitterground_rotten/', '4_capsicum_fresh/', '5_capsicum_rotten/', '6_carrot_fresh/', '7_carrot_rotten/', '8_cucumber_fresh/', '9_cucumber_rotten/', '10_okra_fresh/', '11_okra_rotten/', '12_potato_fresh/', '13_potato_rotten/']
tofile = 'train/'
type = ['images', 'labels']
# 設定兩個資料夾的路徑
for i , item in enumerate(cate):
    folder1 = folder + item + tofile + type[0]
    folder2 = folder + item + tofile + type[1]

    # 找出只存在於每個資料夾中的檔案名稱
    unique_in_folder1, unique_in_folder2 = find_unique_files(folder1, folder2)

    # 輸出結果
    print(f"檔案只存在於 {folder1} 中：")
    for file in unique_in_folder1:
        print(file)

    print(f"\n檔案只存在於 {folder2} 中：")
    for file in unique_in_folder2:
        print(file)
