"""Create a Python script that will search a predetermined directory and list the items within, separating the files and
   directories into two lists that will be printed to the screen."""

import os

inp = input("Enter full directory path(where want to search): ")        # Take Directory path where we want to watch
inp2 = input("Enter directory name(which you want to search): ")        # Take Directory name which we want to find

dirs = []
files = []
r, d, f = next(os.walk(inp))                                            # r=root, d=dir, f=files. os.walk will give list of dirs and files
if inp2 in d:                                                           # If directory exist than get list of sub-directory and files
    r, d, f = next(os.walk("{0}/{1}".format(inp, inp2)))
    dirs = d
    files = f
else:
    print("Directory not found")

print("Directories: ", dirs)
print("Files: ", files)
