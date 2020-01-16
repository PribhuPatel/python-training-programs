try:
    # Take two values from user and find max value
    val1 = int(input("Enter any value = "))
    val2 = int(input("Enter any value = "))
    print("Max value is {0}".format(max(val1, val2)))
except ValueError:
    print("Please Enter a valid number")
