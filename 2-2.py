string = input("Enter String = ")

if len(string)<2:
    print("Empty String")
else:
    a = string[0:2]
    b = string[-2:]

    finalString = a + b
    print(finalString)