try:
    # Get 1 String and 1 Character to search
    string = input("Enter String = ")
    if not len(string):
        raise Exception("Empty String")
    c = input("Enter Character=")
    string = string.lower()  # Convert String and Character both to lower
    c = c.lower()
    count = 0
    for i in string:  # Compare Characters from String with Search Character
        if c == i:
            count = count + 1

    print("Total Count of {0} is {1}".format(c, count))  # Print Search Character
except Exception as error:
    print(error)
