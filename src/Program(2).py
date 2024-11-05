# script to create a lot of files faster

import os


def create_files(base_name, file_extension, start_num, end_num, directory="."):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    for i in range(start_num, end_num + 1):
        filename = f"{base_name}({i}){file_extension}"
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as f:
            f.write(f"File: {filename}\nThis is file number {i}")
        print(f"Created file: {file_path}")

#__main__

file_Name = input("Enter base file name: ")
file_extension = input("Enter file extension: ")
dir_Name = input("Enter a dir: ")
start_Num = int(input("Enter starting num: "))
end_Num = int(input("Enter ending num: "))

create_files(file_Name, file_extension, start_Num, end_Num, dir_Name)
