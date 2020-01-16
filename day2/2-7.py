try:
    # Take String inputs and store it in a list
    inp = int(input("Enter Size of a List="))
    l = list()
    for i in range(0, inp):
        l.append(input("Enter input="))

    # Get search string in variable and Search it in List and Print Index
    search = input("Enter Search String= ")
    print(l.index(search))
    if search in l:
        print("Index = ", l.index(search))
    else:
        raise (Exception("String not Found"))
except Exception as e:
    print(e)
except ValueError:
    print("Enter Valid Number")
