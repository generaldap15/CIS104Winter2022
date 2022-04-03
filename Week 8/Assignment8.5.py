fname = input("Enter file name: ")
count = 0

if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    words = line.split()
    if len(words) < 1 : continue
    if words[0] != 'From' or words[0] == "From:" : continue

    print(words[1])
    count = count + 1


print("There were", count, "lines in the file with 'From' as the first word")
