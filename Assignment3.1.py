hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate:"))
pay = hours * rate

if hours <= 40 :
    pay = hours*rate
else :
    reg = hours*rate
    ovr = (hours - 40) * (rate * 1.5)
    pay= reg + ovr
print ("You made"  ,pay , "dollars")
