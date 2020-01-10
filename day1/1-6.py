asd = input("")
values = asd.split(" ")

n=int(values[0])
c=int(values[1])
b=int(values[2])
cap = b*c
basd = input("")
kad=basd.split(" ")

temp=0
for i in kad:
    if int(i)>cap:
        temp=1
        break

if temp==0:
    print("Yes")
else:
    print("No")