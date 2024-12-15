# Program to print the file names in a dir

import os

directory = '/path/to/your/directory'

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

print("Files in directory:", files)
