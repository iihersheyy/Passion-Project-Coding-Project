#Problem : List all directories and files in a path 

import os

get_dir = "./"

print("Files and Directores in : %s" % get_dir)
for files in os.listdir(get_dir):
    print(files)
