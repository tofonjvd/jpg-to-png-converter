import sys
import os
from PIL import Image

def operation(working_folder, output_folder):
    files = os.listdir(working_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    i = 1
    print(f"{len(files)} pictures have been founded !")
    for file in files:
        print(f"Working on picture {i}")
        if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG"):
            with Image.open(f"{working_folder}\\{file}") as tmp:
                file_name = file.split(".")[0]
                tmp.save(f"{output_folder}\\{file_name}.png", "png")
                tmp.close()
                print(f"Picture number {i} is DONE !")
                i += 1

n = sys.argv

if len(n) > 3:
    print("wrong input! Argument must be like -> python [Your_code.py] [working_dir_path] [output_dir_path]")
else:
    working_dir = n[1]
    output_dir = n[2]
    operation(working_dir, output_dir)

