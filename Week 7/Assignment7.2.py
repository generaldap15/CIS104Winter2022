userin = input("Enter file name: ")

fin = open(userin)

count = 0
total = 0

for line in fin:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    total = total + (float(line[line.find('0'):]))
    #print(count)
    #print(total)
print("Average spam confidence:", total/count)
