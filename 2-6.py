try:
    inp = int(input("Enter Size of Input ="))

    l = list()

    for i in range(0,inp):
        l.append(input("Enter Input = "))

    print(l)
except ValueError:
    print("Please Enter a valid numer")