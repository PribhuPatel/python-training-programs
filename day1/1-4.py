try:
    # Get two values from user and operator to perform given mathematical task
    op1 = int(input("Enter any value = "))
    op2 = int(input("Enter any value = "))
    operator = input("Enter Operator = ")

    # Eval function make mathematical calculation from operator sign
    print(eval("{0} {1} {2}".format(op1, operator, op2)))
except ValueError:
    print("Invalid Input")
except SyntaxError:
    print("Please Enter Valid Operand")
