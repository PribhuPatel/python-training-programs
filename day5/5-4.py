"""Create a json file in following format.
	{
		""folder_name_1"": [filename_1, filename_2, ....],
		""folder_name_2"": [filename_1, filename_2, ....]
		.
		.
		.
	}
   Fetch folder names from the json file and if that folder is present in a predefined location using pythonic way, check if all the files mentioned in the list is present or not.
   Print all the files which are not present in the folder."""
import json
import os

try:
    file = open("demo2.json", "r")
except FileNotFoundError:
    print("Json File not Found")
    exit(1)
json_data = json.loads(file.read())
file.close()

inp = "C:/Users/priyank.bhuva/Desktop/python-training/day2"
r, d, f = next(os.walk(inp))
for i in json_data.keys():
    if i in d:
        root, dirs, files = next(os.walk("{0}/{1}".format(inp, i)))
        new_list = list(set(json_data[i]) - set(files))                     # Subtract list of files available in directory from files listed in json
        print(new_list)
