from PIL import Image
import os

def convert_png_to_jpg_and_delete(png_file, jpg_output):
    try:
        # Open the PNG file
        img = Image.open(png_file)

        # Convert RGBA images (PNG) to RGB (JPEG)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        if img.mode == 'P':
            img = img.convert('RGB')
        # Save as JPEG
        img.save(jpg_output, 'JPEG')

        print(f'{png_file} 轉換成 {jpg_output}')

        # Delete original PNG file
        os.remove(png_file)
        print(f'{png_file} 刪除成功')

    except Exception as e:
        print(f'處理 {png_file} 時發生錯誤: {e}')


def convert_folder_png_to_jpg(folder_path):
    tot = 0
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f'資料夾 {folder_path} 不存在')
            return

        # Get all files in the folder
        files = os.listdir(folder_path)

        # Process each file
        for file in files:
            if file.endswith('.png'):
                tot += 1
                print(tot, end='  ')
                png_file = os.path.join(folder_path, file)
                jpg_output = os.path.join(folder_path, file.replace('.png', '.jpg'))
                convert_png_to_jpg_and_delete(png_file, jpg_output)

    except Exception as e:
        print(f'處理資料夾 {folder_path} 時發生錯誤: {e}')


# 使用範例
if __name__ == '__main__':
    folder_path = './trainfolder/rotten_okra/train/images'  # 資料夾路徑

    convert_folder_png_to_jpg(folder_path)