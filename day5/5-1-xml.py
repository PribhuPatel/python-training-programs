"""Given a xml file(sample.xml) print out all the files and folders hierarchically.
        Take the filename as an argument. Use OOPS concepts.
        Python script should contain class and all the required definitions should be defined within that class.

        (//10.0.1.22/CrestData/UserData/Jay Joshi/Python handson/demo.xml)"""

import xml.etree.ElementTree as ET


class XML:
    def __init__(self):
        self.j = 0
        self.root = ET.parse('demo.xml').getroot()  # Get First Root Element

    def print_files(self, k):
        for i in k:
            if i.tag == "folder":
                if i.tag == "folder":  # If Folder than print Folder name
                    print("\t" * self.j, i.attrib["name"])
                if len(i):  # If Folder has Child Elements than increase j for space and go to find child elements
                    self.j += 1
                    self.print_files(i)
            else:
                print("\t" * self.j, i.attrib["name"])
        self.j -= 1


try:
    xml = XML()
    xml.print_files(xml.root)
except FileNotFoundError:
    print("XML File not in directory")
