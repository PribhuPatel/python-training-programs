string = input("Enter a string =")
newstring = input("Enter Middle String =")

lens =int((len(string)/2))
# print(lens)
if len(string)%2==0:
    string = string[0:lens] + newstring + string[lens:]
else:
    string = string[0:lens] + newstring + string[lens+1:]


print(string)