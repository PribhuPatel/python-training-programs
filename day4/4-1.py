"""Create a python class Author. Create a python class for Programming languages which must inherit Author class.
Create a class which should print the details of given programming language as input."""

# Author Class
class Author:
    def __init__(self, author):
        self.author = author


# Programming_Language class by Inherit Author class
class Programming_language(Author):
    def __init__(self, name, author):
        self.name = name
        super(Programming_language, self).__init__(author)

    def print(self):
        print("The name of the programming language is", self.name, "and the author is", self.author)


# Print or Display Output as Programming Language and Author
class Display:
    def print(self):
        name = input("Enter a programming language: ")
        author = input("Enter author: ")
        language = Programming_language(name, author)
        language.print()


display = Display()
display.print()
