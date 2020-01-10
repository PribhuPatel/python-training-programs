import xml.etree.ElementTree as ET

tree = ET.parse('demo.xml')


class XML:
    def __init__(self):
        self.j = 0
        self.root = ET.parse('demo.xml').getroot()

    def print_files(self, k):
        for i in k:
            if i.tag == "folder" or i.tag == "module":
                if i.tag == "folder":
                    print("\t" * self.j, i.attrib["name"])
                if len(i):
                    self.j += 1
                    self.print_Files(i)
            else:
                print("\t" * self.j, i.attrib["name"])
        self.j -= 1


xml = XML()
xml.print_files(xml.root)
