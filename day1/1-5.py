# Swap and Return values as tuple
def swap(a, b):
    return b,a


try:
    # Take 2 values from user and print it
    val1 = int(input("Enter any value = "))
    val2 = int(input("Enter any value = "))
    print("a={0} and b={1}".format(val1, val2))

    # Swap values using function
    a, b = swap(val1, val2)
    print("a={0} and b={1}".format(val1, val2))
except ValueError:
    print("Enter Valid numbers")
