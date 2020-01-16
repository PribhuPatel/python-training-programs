string = input("Enter a String =")  # Take String as Input

if len(string) > 2:
    if string.endswith("ing"):  # Check end with ing and join ly
        string = string + "ly"
    else:
        string = string + "ing"  # If not ing at the end of string add ing

print(string)