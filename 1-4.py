try:
    op1 = int(input("Enter any value = "))
    op2 = int(input("Enter any value = "))
    operand = input("Eneter Operator = ")
    print(eval("{0} {1} {2}".format(op1,operand,op2)))
except ValueError:
    print("Invalid Input")
except SyntaxError:
    print("Please Enter Valid Operand")