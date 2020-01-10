import re


class FindFiles:
    def __init__(self,filename):
        file = open(filename, 'r')
        self.lines = file.readlines()
        file.close()

    def print_hierarchy(self):

        file_pat = re.compile(r"(file) name=\"(.*?)\"")
        folder_with_end_pat = re.compile(r"(folder) name=\"(.*?)\" (.*)(\/)")
        folder_pat = re.compile(r"(folder) name=\"(.*?)\"")
        folder_end_pat = re.compile(r"</(folder)>")

        j = 0
        for i in self.lines:
            mat = folder_with_end_pat.search(i) or file_pat.search(i) or folder_pat.search(i)
            folder_mat = folder_end_pat.search(i)
            if mat:
                if mat.group(1) == "folder":
                    print("\t" * j, mat.group(2))
                    if mat.lastindex == 2:
                        j += 1
                if mat.group(1) == "file":
                    print("\t" * j, mat.group(2))
            if folder_mat:
                j -= 1

inp = input("Enter File name: ")

pattern_match = FindFiles(inp)
pattern_match.print_hierarchy()