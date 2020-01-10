# import io, json
#
# file = open("6-1.json","r")
#
# file_json = {
#     'name':file.name,
#     'mode':file.mode,
#     'data':file.read()
# }
#
# file.close()
#
# with open("6-2.json","w") as f:
#     json.dump(file_json, f)
#
# with open("6-2.json","r") as f:
#     loaded_json = json.load(f)
#     file2 = io.BytesIO(bytes(loaded_json["data"],encoding="utf-8"))
#     file2.name=loaded_json["name"]
#     file2=io.TextIOWrapper(file2)
#
# print(file2.read())
# print(file2.name)
# print(file2.__class__)
# print(file2.closed)
#
# file2.close()


# file = open("6-2.json","r")
# print(file.__class__)
#
# print(file.mode)
# print(file.__init_subclass__())
import io,json
# io.TextIOWrapper()

# with open("6-2.json","r") as f:
#     loaded_json = json.load(f)
#     file2 = io.BytesIO(bytes(loaded_json["data"],encoding="utf-8"))
#     file2.name=loaded_json["name"]
#     file2=io.TextIOWrapper(file2)
#
# print(file2.mode)

import pickle

import cls as cls

# file=open("6-1.json","r")
with open("6-2.pickle","wb") as f:
    pickle.dump("asdad",f)
# file.close()

# if file is object:
#     print("Object")
#
# if file is cls:
#     print("Class")