"""Write a function that takes json file(demo.json) as an input and return value for any of the requested key.
        (The key may be at any level)
        =============
        sample input
        =============

        md5Hex

        =============
        desired ouput
        =============

        377d484478843e5e2d8b7eb935cbf598

(\\10.0.1.22\CrestData\UserData\Jay Joshi\Python handson\demo.json)"""

import re


class FindFiles:
    def __init__(self, filename):
        file = open(filename, 'r')
        self.lines = file.read().replace('\n', '')
        self.lines = self.lines.replace(' ', '')
        print(self.lines)
        file.close()

    def find_key(self, key):
        file_pat1 = re.compile(r"\"{0}\":(\[(.*?)\])".format(key))
        file_pat2 = re.compile(r"\"{0}\":(\{{(.*?)\}})".format(key))
        file_pat3 = re.compile(r"\"{0}\":\"(.*?)\"(\}}|\,)".format(key))
        file_pat4 = re.compile(r"\"{0}\":(.*?)(\}}|\,)".format(key))
        mat = file_pat1.search(self.lines) or file_pat2.search(self.lines) or file_pat3.search(
            self.lines) or file_pat4.search(self.lines)
        if mat:
            print(mat.group(1))
        else:
            print("Key not Found")


inp = input("Enter File name: ")

pattern_match = FindFiles(inp)

inp = input("Enter  Key: ")
pattern_match.find_key(inp)
# pattern_match = FindFiles("demo.json")
# pattern_match.find_key("data")
