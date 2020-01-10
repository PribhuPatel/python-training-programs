a = int(input("Enter Size of a List="))

l=list()
for i in range(0,a):
    l.append(int(input("Enter input")))

# average = sum(l)/a
print(sum(l)/a)