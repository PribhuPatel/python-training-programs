# Take String as Input
string = input("Enter String = ")

# Check String Length
if len(string)<2:
    print("Empty String")
else:
    a = string[0:2]  # Slice string from index 0-2
    b = string[-2:]  # Slice string from 2nd last index

    finalString = a + b  # Join String
    print(finalString)
