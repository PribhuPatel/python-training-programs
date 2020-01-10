import re,json

class FindFiles:
    def __init__(self,filename):
        file = open(filename, 'r')
        self.lines = file.read().replace('\n','')
        self.lines = self.lines.replace(' ', '')
        print(self.lines)
        file.close()

    def find_key(self,key):
        file_pat1 = re.compile(r"\"{0}\":(\[(.*?)\])".format(key))
        file_pat2 = re.compile(r"\"{0}\":(\{{(.*?)\}})".format(key))
        file_pat3 = re.compile(r"\"{0}\":\"(.*?)\"(\}}|\,)".format(key))
        file_pat4 = re.compile(r"\"{0}\":(.*?)(\}}|\,)".format(key))
        mat= file_pat1.search(self.lines) or file_pat2.search(self.lines) or file_pat3.search(self.lines) or file_pat4.search(self.lines)
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