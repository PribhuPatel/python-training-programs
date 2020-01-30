import httplib2, json
from threading import Thread, Lock

lock = Lock()
http = httplib2.Http()
res, cont = http.request("http://localhost:5000/get-end", method="GET")
cont = cont.decode(encoding="UTF-8").strip("[]").replace("\'", "").replace(" ", "").split(",")
i = 0


class Create_Json(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        self.create_json()

    def create_json(self):
        for t in range(0, self.num):
            global i
            with lock:
                k = i
                i += 1
            http = httplib2.Http()
            res, con = http.request("http://localhost:5000/json_files/" + cont[k], method="GET")
            with open(f"json_files2/{cont[k]}", "w") as f:
                f.write(con.decode(encoding="UTF-8"))
            del http


num = len(cont) // 10
try:
    for k in range(0, num):
        thread = Create_Json(10)
        thread.start()

    thread = Create_Json(len(cont) - (num * 10))
    thread.start()
except Exception as e:
    print(e)
    exit(1)
