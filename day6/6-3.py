"""Use complex classes created in 'Classes' module and serialize-deserialize objects of them."""

import pickle


class First:  # Class First
    first = None

    def __init__(self, first):
        self.first = first

    def show(self):
        print("First : ", self.first)


class Second(First):  # Class Second inheritate Class First
    second = None

    def __init__(self, first, second):
        super().__init__(first)
        self.second = second

    def show(self):
        super().show()
        print("Second : ", self.second)


class Third(Second):  # Class Third inheritate Class Second
    third = None

    def __init__(self, first, second, third):
        super().__init__(first, second)
        self.third = third

    def show(self):
        super().show()
        print("third : ", self.third)


# Classes Ends

def serializePickle(data):
    with open('6-3.pickle', 'wb') as PFile:
        pickle.dump(data, PFile)


def deserialize_Pickle():
    with open('6-3.pickle', 'rb') as PFile:
        return pickle.load(PFile)


try:
    print("Please Enter Three Value:")
    first = input("First : ")
    second = input("Second : ")
    third = input("Third : ")

    third_obj = Third(first, second, third)

    serializePickle(third_obj)

    third_pickle = deserialize_Pickle()
    third_pickle.show()

except ValueError:
    print("Please Enter valid input")
except TypeError:
    print("Problem in Serialization or Deserialization Occured")
