try:
    # Take a string remove (.) and split
    string = input("Enter Full String = ")
    if not len(string):
        raise Exception("Enter at least one character")
    string = string.lower()
    string = string.replace(".", "")
    split = string.split(" ")

    # Save all the characters as key and count as value
    dic = dict()
    for i in split:
        if i in dic.keys():
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    print(dic)
except Exception as e:
    print(e)
