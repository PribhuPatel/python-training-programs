try:
    # Take Number as input and convert it to int type
    inp = int(input("Enter any number = "))

    # Compare Number and Print output accordingly
    if 0 < inp < 10:
        print("Small")
    elif inp < 100:
        print("Medium")
    elif inp < 1000:
        print("Large")
    else:
        print("Invalid")

except ValueError:
    print("Please Enter a valid number")
