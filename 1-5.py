def swap(a, b):
    return b,a
try:
    val1 = int(input("Enter any value = "))
    val2 = int(input("Enter any value = "))

    print("a={0} and b={1}".format(val1,val2))

    a, b = swap(val1, val2)
    print("a={0} and b={1}".format(val1, val2))
except ValueError:
    print("Enter Valid numbers")


