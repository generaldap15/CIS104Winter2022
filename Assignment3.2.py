hours = input("Enter Hours: ")
rate = input("Enter Rate:")
try :
    hrs = float(hours)
    rte = float(rate)
except :
    print ("Please enter a number")
    quit()

if hrs <= 40 :
        pay = hrs *rte
else :
    reg = hrs*rte
    ovr = (hrs - 40) * (rte * 1.5)
    pay= reg + ovr

print ("You made"  ,pay , "dollars")
