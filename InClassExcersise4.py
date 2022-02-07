a= input("Input First Value")
b= input("Input Second Value")
c= input("Input Third Value")

def value3(a, b, c):
    if a>b and a>c:
        print("First Value is the Biggest")

    elif b>a and b>c:
        print("Second Value is the Biggest")

    elif c>a and c>b:
        print("Third Value is the Biggest")

value3(a,b,c)
