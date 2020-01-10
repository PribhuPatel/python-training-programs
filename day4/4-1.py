class Author:
    def __init__(self, author):
        self.author = author


class Programming_language(Author):
    def __init__(self, name, author):
        self.name = name
        super(Programming_language, self).__init__(author)

    def print(self):
        print("The name of the programming language is", self.name, "and the author is", self.author)


class Display:
    def print_display(self):
        name = input("Enter a programming language")
        author = input("Enter author")
        language = Programming_language(name, author)
        language.print()


display = Display()
display.print_display()
