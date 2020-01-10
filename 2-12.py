try:
    inp= int(input("Enter Number of Students="))
    l=list()
    for i in range(0,inp):
        stu=dict()
        stu['rollno'] = int(input("Roll no of Student="))
        stu['firstname'] =input("First Name of Student=")
        stu['lastname'] = input("Last Name of Student=")
        l.append(stu)

    x= int(input("Select \n1.Roll no\n2.First name\n3.Last name\nEnter Choice="))
    keys = {1:'rollno',2:'firstname',3:'lastname'}
    l = sorted(l, key=lambda k: k[keys[x]])

    print(l)
except ValueError:
    print("Enter Valid Input")
