try:
    # Take number of elements and save it to list
    inp = int(input("Enter Size of a List="))
    l = list()
    for i in range(0, inp):
        l.append(int(input("Enter input=")))

    # Make sum of list elements and devide by number to get average
    print(sum(l) / inp)
except ValueError:
    print("Enter Valid number")
except ZeroDivisionError:
    print("Size cannot be Zero")
