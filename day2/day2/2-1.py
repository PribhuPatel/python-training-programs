string = input("Enter String = ")
c = input("Enter Character=")
string =string.lower()
c= c.lower()
count=0
for i in string:
    if c==i:
        count=count+1

print("Total Count of {0} is {1}".format(c,count))