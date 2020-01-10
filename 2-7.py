try:
    inp = int(input("Enter Size of a List="))

    l=list()
    for i in range(0,inp):
        l.append(input("Enter input="))

    search = input("Enter Search String= ")
    if search in l:
        print("Index = ", l.index(search))
    else:
        raise (Exception("String not Found"))
except Exception as e:
    print(e)