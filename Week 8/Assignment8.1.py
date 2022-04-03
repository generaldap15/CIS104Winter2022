t = ['Jade', 'David', 'James', 'Gerald', 'Bob']
t2 = ['Jade', 'David', 'James', 'Gerald', 'Bob']

def chop():


    t.remove('Jade')

    t.remove('Bob')

    return None

chop()


def middle(infunction):

    newlist = infunction[1:]

    'print(id(newlist))'
    'print(id(infunction))'

    del newlist[-1]

    return newlist
    
returnedValue = middle(t2)

print(returnedValue)
print(t2)
