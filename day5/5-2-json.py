""" Write a function that takes json file(demo.json) as an input and return value for any of the requested key.
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

import json


# If value will be dict and list it will again go for find a key in child dictionary and also print key-value found on current dictionary
def find_key(value, key):
    if type(value) == dict:
        if key in value.keys():
            print(key, " = ", value[key])
        for i in value:
            find_key(value[i], key)
    elif type(value) == list:
        for i in value:
            find_key(i, key)
    else:
        return


# Take File name as Input
inp = input("Enter File name: ")

try:
    with open(inp) as file:
        json_data = json.loads(file.read())
except FileNotFoundError:
    print("File not Found on current Directory")
    exit(1)

# Key to search in JSON
inp = input("Enter  Key: ")
find_key(json_data, inp)
