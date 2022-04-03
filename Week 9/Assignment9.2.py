fhand = open('mbox-short.txt')
days = dict()

for line in fhand:
    words = line.split()
    
    if len(words) < 3 or words[0] != 'From'  : continue

    if words[2] not in days:
        days[words[2]] = 1
    else:
        days[words[2]] += 1


print(days)
