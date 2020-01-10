import json

def findKey(key,findkey):
    if type(key)==dict:
        if findkey in key.keys():
            print(findkey," = ",key[findkey])
        for i in key:
            findKey(key[i],findkey)
    elif type(key)==list:
        for i in key:
            findKey(i,findkey)
    else:
        return


inp = input("Enter File name: ")


with open(inp) as file:
    json_data = json.loads(file.read())

inp = input("Enter  Key: ")
findKey(json_data,inp)