import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        file_extension = filename.split('.')[-1]
        folder_name = file_extension.upper() + "_FILES"
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            shutil.move(file_path, os.path.join(folder_path, filename))

def main():
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
    print("Files organized successfully.")

if __name__ == "__main__":
    main()
