userin = input("Enter file name: ")
print(userin)

fin = open(userin)

for line in fin:
    print(line.upper().strip())
