import re
count = 0
finp = input("Please Enter a File Name:")
hand = open(finp)
inp = input('Please Enter a VALID Regular Expression:')

for line in hand:
    line = line.rstrip()
    if re.search(inp, line):
        count = count + 1
print('Your file has', count, 'lines that matched', inp)
