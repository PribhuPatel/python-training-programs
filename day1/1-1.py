try:
    # Take number of input values and inputs from user
    inp = int(input("Enter any number = "))
    x = []
    for i in range(0, inp):
        x.append(input("Enter input no. " + str(i) + " = "))

    # Print Input done by user
    for i in range(0, inp):
        print(x[i])
except ValueError:
    print("Please Enter a valid number")
