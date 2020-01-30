"""Try serializing file handler object."""

import io
import json

try:
    file = open("6-1.json", "r")
except FileNotFoundError:
    print("File not Found")
    exit(1)
file_json = {
    'name': file.name,
    'data': file.read()
}

file.close()

with open("6-2.json", "w") as f:
    json.dump(file_json, f)

with open("6-2.json", "r") as f:
    loaded_json = json.load(f)
    file2 = io.BytesIO(bytes(loaded_json["data"], encoding="utf-8"))
    file2.name = loaded_json["name"]
    file2 = io.TextIOWrapper(file2)

print(file2.read())
print(file2.name)
print(file2.__class__)
print(file2.closed)

file2.close()
print(file2.closed)

"""Pickle cannot Serialize all type of objects. There are limitations.
It cannot serialize Objects wich are temporary with program runtime."""
