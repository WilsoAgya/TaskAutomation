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
3. Set conditionals that determine which file type they are
4. Rename the file names and print them,clean it and add the file type
5. Rename the physical files and place them in a new folder titled "files_updated"


RENAMING THE FILES AND PUTTING THEM INTO A NEW FOLDER:
1. MAKE A NEW FOLDER
2. Access the new folder
3. Iteratively copy the same files with their new names



"""

from pathlib import Path
import os
import shutil

prompt_msg = 'Enter the folder name that holds your files: '
newFolder_promptmsg = 'Enter the folder for your renamed files: '
inputfoldername = ""
directory_path = ""
destination_path= ""
path = './'
newFoldername = ""

prefixes = {
    'pdf':'document_', 'docx':'document_',
    'txt':'text_',
    'py':'code_',
    'jfif':'img_',
    'jpg':'img_',
    'png':'img_'
}

def input_newfolder_name():

    global inputfoldername,newFoldername,directory_path,destination_path

    #Until the inputFoldername is valid or exists ask the user again for the inputFoldername
    #If the input foldername path exists create a new folder named the value at was inputted for newFoldername
    while True:
        inputfoldername = input("Enter the directory that has the files you'd like to rename: ")

        if os.path.exists(inputfoldername):
            print(f"Directory found: {inputfoldername}")
            directory_path=Path(f'./{inputfoldername}')
            while True:
                newFoldername = input("Enter the folder for your renamed files: ")
                if os.path.exists(newFoldername):
                    print(f"Directory already exists please try again")
                else:
                    os.mkdir(newFoldername)
                    destination_path=Path(f'./{newFoldername}')
                    break
            break
        else:
            print("Path does not exist. Please try again")


#Copy and rename the old files into a new folder
def copy_and_rename(src_path, dest_path, new_name):

    new_path = os.path.join(dest_path,new_name)

    # Copy the file
    shutil.copy(src_path, new_path)
    new_path = destination_path

    print(f"Copied and renamed to: {new_path}")


#Iteravely go through each file in the old folder and check which type of file it is. Make the necessary changes to the names
#Call the copy_and_rename function to add the newly named files into the destination directory
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


input_newfolder_name()
check_name()