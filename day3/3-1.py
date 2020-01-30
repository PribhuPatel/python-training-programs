"""Write a function that given a string it returns true if the string is a number. As there might be several
definitions of what is the number create several solutions one for each definition: Non negative integer. Integer.
Real number. In scientific notation. (something like this: 2.123e4 )"""


def check_str(string):
    if len(string.split(" ")) != 1:
        print("Not Number")
        return False
    else:
        if string.isdigit() or (string[1:].isdigit() and string[0] == "-"):
            abc = int(string)
            if abc >= 0:
                print("Non-Negative Integer Value")
            else:
                print("Negative Integer")
        else:
            try:
                abc = float(string)
            except ValueError:
                return False                            # Return False if Str cannot convert to float means it is not a float value
            print(abc)
            if string.lower() == string.upper():        # If lower!=Upper than it has valid Scientific Notation
                print("Float Number")
            else:
                print("Scientific Notation")
        print(abc)
        return True


inp_string = input("Enter any number: ")
print("String is Number" if check_str(inp_string) else "String is not a Number")
