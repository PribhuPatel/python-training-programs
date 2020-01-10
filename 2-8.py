try:
    inp = int(input("Enter Size of a List="))

    l=list()
    for i in range(0,inp):
        l.append(int(input("Enter input=")))

    # average = sum(l)/a
    print(sum(l)/inp)
except ValueError:
    print("Enter Valid number")
except ZeroDivisionError:
    print("Size cannot be Zero")