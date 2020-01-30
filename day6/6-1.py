"""Create a simple class(e.g. Employee) with some attributes(e.g. name, age, gender) and serialize-deserialize objects
using JSON and Pickle and compare both of these methods. (Take values from user as inputs at the first time and to
update them at the second time after deserialize and then serialize them) """

import pickle


class Employee:

    def __init__(self, entries):                    # Entries is a dictionary
        self.name = ""
        self.age = 0
        self.gender = ""
        self.__dict__.update(entries)               # Update object values as dictionary update

    def update_name(self, name):
        self.name = name


name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")

employee = Employee({"name": name, "age": age, "gender": gender})

with open("6-1.pickle", "wb") as f:                 # Serialize object with pickle
    pickle.dump(employee, f)

with open("6-1.pickle", "rb") as f:                 # Deserialize object with pickle
    employee1 = pickle.load(f)

name = input("Enter new Name: ")
employee1.update_name(name)

import json

with open("6-1.json", "w") as f:                    # Serialize object with json with dictionary format
    json.dump(employee1.__dict__, f)

with open("6-1.json", "r") as f:                    # # Deserialize object with json in dictionary format and convert to an object
    employee2 = Employee(json.load(f))

name = input("Enter new Name: ")
employee2.update_name(name)

print(employee.__dict__)
print(employee1.__dict__)
print(employee2.__dict__)


"""Pickle can serialize objects with its methods. But Json can store data in dictionary format or as a List"""
"""We can not read data perfectly from pickle file but we can read Json file as it stores data in UTF-8 String format"""
