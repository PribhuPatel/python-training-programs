string = input("Enter a String =")

if len(string) > 2:
    if string.endswith("ing"):
        string = string + "ly"
    else:
        string = string + "ing"

print(string)