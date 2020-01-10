a = int(input("Enter any number = "))

x = []
for i in range(0,a):
    x.append(input("Enter input no. " + str(i) + " = "))

for i in range(0,a):
    print(x[i])