max = None
min = None

while True :
    x = input('Enter Number:')
    if x == 'done' :
        break
    try:
        ix = int(x)
    except:
        print ('Invalid Input')
        continue

    if max == None :
        max = ix

    if max < ix :
        max = ix

    if min == None :
        min = ix

    if min > ix :
        min = ix


print (max, min)
