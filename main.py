import sys
import os
from PIL import Image


def operation(working_folder, output_folder):
    # Make a list of our files in working dirctory
    files = os.listdir(working_folder)

    # Checking if the output exists. if not, so make it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Pointer for the number of image we're working, but in a dummy way
    i = 1
    print(f"{len(files)} pictures have been founded !")

    for file in files:
        print(f"Working on picture {i}")

        # Check if the working file is a JPG file
        if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG"):
            with Image.open(f"{working_folder}\\{file}") as tmp:
                # Splitting the JPG file extension for better readability
                file_name = os.path.splitext(file)[0]

                # Converting the image
                tmp.save(f"{output_folder}\\{file_name}.png", "png")
                tmp.close()
                print(f"Picture number {i} is DONE !")
                i += 1


# Getting arguments from the command line
n = sys.argv

if len(n) > 3:
    print("wrong input! Argument must be like -> python [Your_code.py] [working_dir_path] [output_dir_path]")
else:
    working_dir = n[1]
    output_dir = n[2]
    operation(working_dir, output_dir)
