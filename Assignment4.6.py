hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate:"))

def computepay():

    pay = hours * rate

    if hours <= 40 :
        pay = hours*rate
        print ("You made", pay, "dollars")
    else :
        reg = hours*rate
        ovr = (hours - 40) * (rate * 0.5)
        pay= reg + ovr
        print ("You made",pay, "dollars")

computepay()
