try:
    # Take first line input
    first_input = input()
    values = first_input.split(" ")

    if len(values) != 3:
        raise Exception("Please Enter valid N C B")

    n = int(values[0])
    c = int(values[1])
    b = int(values[2])
    total_boat_capacity = b * c  # Calculate total boat capacity per trip

    # Take Second Line input
    second_input = input()
    trips = second_input.split(" ")

    if len(trips) != n:
        raise Exception("Please Enter valid Number of trips")
    temp = 0
    for i in trips:  # Compare capacity for each trip
        if int(i) > total_boat_capacity:
            temp = 1
            break

    # Print Yes or No
    if temp == 0:
        print("Yes")
    else:
        print("No")
except ValueError:
    print("Please Enter Valid Space separated numbers")
except Exception as e:
    print(e)
