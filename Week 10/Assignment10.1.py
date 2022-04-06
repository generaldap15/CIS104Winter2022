fhand = open('mbox-short.txt')
email_adresses = dict()

for line in fhand:
    words = line.split()

    if len(words) < 3 or words[0] != 'From'  : continue

    if words[1] not in email_adresses:
        email_adresses[words[1]] = 1
    else:
        email_adresses[words[1]] += 1

#print(email_adresses)

email_lst = list()
for k,v in email_adresses.items():
    email_lst.append((v,k))

email_lst = sorted(email_lst, reverse=True)

for k,v in email_lst[:1]:
    print(v,k)
