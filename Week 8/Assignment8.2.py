fhand = open('mbox-broken.txt')

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3 : continue
    if len(words) == 0 : continue
    if words[0] != 'From' : continue


    print(words[2])
