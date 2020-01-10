try:
    inp = int(input("Enter any number = "))
    if 0<inp<10:
        print("Small")
    elif inp<100:
        print("Medium")
    elif inp<1000:
        print("Large")
    else:
        print("Invalid")

except ValueError:
    print("Please Enter a valid number")