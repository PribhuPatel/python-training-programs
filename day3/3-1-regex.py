"""Write a function that given a string it returns true if the string is a number. As there might be several
definitions of what is the number create several solutions one for each definition: Non negative integer. Integer.
Real number. In scientific notation. (something like this: 2.123e4 )"""

import re


def check_number(string):
    match = re.match("^(?P<negative>\-)?\d+(?:\.(?P<real>\d+|(?P<scientific_notation>[\dEe\+\-]+)))?$",string)

    if match:
        groups = match.groupdict()
        if groups["negative"]:
            print("Negative",end=" ")
        if groups["scientific_notation"]:
            print("Scientific Notation")
        elif groups["real"]:
            print("Real Value")
        else:
            print("Integer Value")
        return True
    else:
        return False


inp_string = input("Enter any number: ")
print("String is Number" if check_number(inp_string) else "String is not a Number")