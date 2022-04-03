fhand = open('mbox-short.txt')
email_adresses = dict()

for line in fhand:
    words = line.split()

    if len(words) < 3 or words[0] != 'From'  : continue

    if words[1] not in email_adresses:
        email_adresses[words[1]] = 1
    else:
        email_adresses[words[1]] += 1


print(email_adresses)
