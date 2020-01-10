class Employee:

    def __init__(self, entries):
        # print(entries)
        self.name = ""
        self.age = 0
        self.gender = ""
        # self.name = entries["name"]
        # self.age = entries["age"]
        # self.gender = entries["gender"]
        self.__dict__.update(entries)

    def update_name(self, name):
        self.name = name


name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")

employee = Employee({"name": name, "age": age, "gender": gender})

# employee = Employee(name=name,age=age,gender=gender)
import pickle

with open("6-1.pickle", "wb") as f:
    pickle.dump(employee, f)

with open("6-1.pickle", "rb") as f:
    employee1 = pickle.load(f)

name = input("Enter new Name: ")
employee1.update_name(name)

import json

with open("6-1.json", "w") as f:
    json.dump(employee1.__dict__, f)

with open("6-1.json", "r") as f:
    employee2 = Employee(json.load(f))

name = input("Enter new Name: ")
employee2.update_name(name)

print(employee.__dict__)
print(employee1.__dict__)
print(employee2.__dict__)
