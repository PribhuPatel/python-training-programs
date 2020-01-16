string = input("Enter a string =")
middle_string = input("Enter Middle String =")

len = int((len(string) / 2))  # Find Length of a string

if len(string) % 2 == 0:  # add middle string to main string at middle index
    string = string[0:len] + middle_string + string[len:]
else:
    string = string[0:len] + middle_string + string[len + 1:]

print(string)
