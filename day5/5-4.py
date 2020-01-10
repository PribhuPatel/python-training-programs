import re,json,os

file = open("demo2.json","r")
json_data = json.loads(file.read())
file.close()
print(repr(json_data))

print(type(json_data))
inp = "C:/Users/priyank.bhuva/Desktop/python-training/day2"
r,d,f = next(os.walk(inp))
for i in json_data.keys():
    if i in d:
        root,dir,files = next(os.walk("{0}/{1}".format(inp,i)))
        new_list=list(set(json_data[i])-set(files))
        print(new_list)