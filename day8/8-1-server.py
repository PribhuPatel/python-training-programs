"""Create a server client application
Server will have the following endpoints
   a. An endpoint which returns a random json content with a filename. Where the filename will be the first line of the response and the content will be 2nd line of the response
        Sample response:
             file_1.json
             {""ransom_url"": ""abc.com"", ""files_affected"": ""some.exe"", ""ransomType"": ""aaa""}
   b. An endpoint which returns a list of dynamically generated #a endpoint's url. (the list size should be at least 1000)

Client will do the following things
   p. It will first request #b endpoint of server and will get list of endpoints to call
   q. It will request all endpoint mentioned in #b response and will fetch the json data using #a endpoint
   r. The json data should be stored in a json file with name & content mentioned in #a endpoint's response

Expected Output:
- A folder will at least 1000 json files created
- Space & Time complexity should be handled for the server & client."""

from flask import Flask, json
import random, os
from threading import Thread, active_count, enumerate

app = Flask(__name__, static_folder="json_files")


class CreateJson(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        self.create_json()

    def create_json(self):
        file_name = random_string(8)
        json_text = {"ransom_url": random_string(10), "files": random_string(5), "ransom_type": random_string(4)}
        print(json_text)
        with open(f"json_files/{file_name}.json", "w") as f:
            json.dump(json_text, f)


def random_string(length):
    abc = "abcdefghijklmnopqrstuvwxyz1234567890"
    string = str("".join(abc[random.randint(1, len(abc) - 1)] for i in range(length)))
    return string


@app.route("/create-end", methods=["GET"])
def create_json():
    for i in range(0, 1000):
        thread = CreateJson()
        thread.start()
    return "Started"


@app.route("/check-end", methods=["GET"])
def check_json():
    print(enumerate())
    return str(active_count())


@app.route("/get-end", methods=["GET"])
def get_list():
    r, d, f = next(os.walk("json_files"))
    return str(f)


app.run(port=5000)
