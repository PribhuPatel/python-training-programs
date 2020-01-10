a = int(input("Enter any value = "))
b = int(input("Enter any value = "))

print("a={0} and b={1}".format(a,b))


def swap(a, b):
    return b,a


a,b = swap(a,b)


print("a={0} and b={1}".format(a,b))
