fhand = open('words.txt')
dict1 = dict()
count = 0
for line in fhand:
    sline = line.split()
    #print(sline)

    for word in sline:
        if word in dict1: continue
        dict1[word] = count
        count = count + 1



print(dict1)

if "do" in dict1:
    print("true")
else:
    print("false")
