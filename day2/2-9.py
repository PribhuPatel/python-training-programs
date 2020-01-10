string = input("Enter Full String = ")
string=string.lower()
string=string.replace(".","")
split = string.split(" ")


dic = dict()

for i in split:
    if i in dic.keys():
        dic[i] = dic[i]+1
    else:
        dic[i]=1


print(dic)