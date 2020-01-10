import re,os


inp = input("Enter full directory path(where want to search): ")
inp2 = input("Enter directory name(which you want to search): ")


dirs=[]
files=[]
r,d,f= next(os.walk(inp))
if inp2 in d:
    r, d, f = next(os.walk("{0}/{1}".format(inp,inp2)))
    dirs=d
    files = f
else:
    print("Directory not found")

print("Directories: ",dirs)
print("Files: ",files)