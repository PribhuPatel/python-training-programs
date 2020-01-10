a = int(input("Enter Size of a List="))

l=list()
for i in range(0,a):
    l.append(input("Enter input"))

b = input("Enter Search String= ")
print(l.index(b))