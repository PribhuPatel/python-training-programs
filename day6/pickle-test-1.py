import pickle

arr = [10,50]

with open("pickle-test-1.pickle","wb") as d:
    pickle.dump(arr,d)


with open("pickle-test-1.pickle","rb") as d:
    arr2=pickle.load(d)

print(arr2)

import json
with open("pickle-test-1.json","w") as d:
    json.dump(arr,d)


with open("pickle-test-1.json","r") as d:
    arr3=json.load(d)

print(arr3)