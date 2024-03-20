from PIL import Image
import fileinput
import sys
import os
    
def convert_image(file, output_format='webp'):
    output_file = str(file).split(".")[0] + "." + output_format
    image = Image.open(file)
    image.save(output_file, format=output_format)

def replce_img_url(file, find_text, replace_text=".webp"):
    with fileinput.FileInput(file, inplace=True, encoding='cp437') as file:
        for line in file:
            sys.stdout.write(line.replace(find_text, replace_text))

def get_all_files_(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        file_paths.extend([os.path.join(root, file) for file in files])
    return file_paths


def main():
    current_directory = os.getcwd()
    files_list = get_all_files_(current_directory)
    img_error_files = []
    rename_error_files = []
    print("Proccesing files")
    for file in files_list:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            try:
                convert_image(file)
                os.remove(file)
            except:
                img_error_files.append(file)
    
    for file in files_list:
        if file.lower().endswith(('.js','.html','.css','.php')):
            try:
                replce_img_url(file=file, find_text=".png", replace_text=".webp")
                replce_img_url(file=file, find_text=".jpg", replace_text=".webp")
                replce_img_url(file=file, find_text=".jpeg", replace_text=".webp")
            except:
                rename_error_files.append(file)
    

    print("Image Process Completed\nError Files are:\n".join(str(file) for file in img_error_files))
    print("Rename Process Completed\nError Files are:\n".join(str(file) for file in rename_error_files))
    
main()