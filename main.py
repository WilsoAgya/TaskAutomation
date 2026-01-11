"""
Objective:
Create a script that organizes items by checking which type of file the item is and renaming the title of the file and adding its type to the beginning of it

Requirements:
ONLY USE PYTHON BUILT IN LIBRARIES
- Check which type of file an item is
- Return the items with their names starting with what type of file they are

Algorithm
1. Import folder
2. Map out all file names
3. Set checks that determine which file type they are
4. Rename the file names and print them and clean it and add the file type
5. Rename the physiical files and place them in a new folder titled "files_updated"


RENAMING THE FILES AND PUTTINIG THEM INTO A NEW FOLDER:
1. MAKE A NEW FOLDER
2. Access the new folder
3. Iteratively copy the same files with their new names
"""

from pathlib import Path
import os
import shutil

directory_path = Path('./files')
path = './'
newFoldername = input("Enter the folder name for your renamed files: ")

prefixes = {
    'pdf':'document_', 'docx':'document_',
    'txt':'text_',
    'py':'code_',
    'jfif':'img_',
    'jpg':'img_',
    'png':'img_'
}



def copy_and_rename(src_path, dest_path, new_name):

    new_path = os.path.join(dest_path,new_name)
    # Copy the file
    shutil.copy(src_path, new_path)

    print(f"Copied and renamed to: {new_path}")



def check_name():

    for filename in os.listdir(directory_path):
        src_file = os.path.join(directory_path,filename)
        new_filename = filename.replace(" ","_")

        for extension, prefix in prefixes.items():
            if new_filename.endswith('.' + extension):
                new_filename = prefix + filename
                break

        copy_and_rename(src_file,newFoldername,new_filename)


        print(new_filename)



def input_folder_name():
    if os.path.exists(newFoldername):
        print(f"Directory '{newFoldername}' already exists.")
    else:
        os.mkdir(newFoldername)
        print(f"Directory '{newFoldername}' created.")



input_folder_name()
check_name()