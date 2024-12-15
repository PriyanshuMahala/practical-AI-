# Program to create a new dir in a dir

import os

new_directory = 'new_folder'

if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created!")
else:
    print(f"Directory '{new_directory}' already exists.")
