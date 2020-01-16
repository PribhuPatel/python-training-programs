try:
    inp = int(input("Enter Size of Input ="))  # Take number of inputs

    l = list()  # List Declared

    for i in range(0, inp):
        l.append(input("Enter Input = "))  # Append inputs to list

    print(l)  # Print List
except ValueError:
    print("Please Enter a valid number")
