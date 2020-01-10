try:
    first_input = input()
    values = first_input.split(" ")

    # if len(values)!= 3:
    #     raise WrongInputError("Please Enter valid N C B")
    if len(values) != 3:
        raise Exception("Please Enter valid N C B")

    n=int(values[0])
    c=int(values[1])
    b=int(values[2])
    total_boat_capacity = b*c
    second_input = input()
    trips=second_input.split(" ")

    if len(trips)!=n:
        raise Exception("Please Enter valid Number of trips")
    temp=0
    # print(trips)
    for i in trips:
        if int(i)>total_boat_capacity:
            temp=1
            break

    if temp==0:
        print("Yes")
    else:
        print("No")
except Exception as e:
    print(e)
except ValueError:
        print("Plesae Enter Valid Space saperated numbers")