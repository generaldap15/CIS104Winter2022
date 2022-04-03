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

times_used = -1
the_mc_email_adress = None
for k,v in email_adresses.items():
    #print(k,v)
    if v > times_used:
        times_used = v
        the_mc_email_adress = k

print(the_mc_email_adress, times_used)
