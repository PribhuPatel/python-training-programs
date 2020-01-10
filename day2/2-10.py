a= int(input("Enter Number of Students="))
l=list()
for i in range(0,a):
    stu=dict()
    stu['name'] =input("Name of Student=")
    stu['marks'] = int(input("Marks of Student="))
    l.append(stu)

newlist = sorted(l, key=lambda k: k['marks'],reverse=True)
second_high=newlist[1]['marks']

for i in range(1,len(newlist)):
    if newlist[i]['marks']==second_high:
        print(newlist[i])
    if newlist[i]['marks']<second_high:
        break



