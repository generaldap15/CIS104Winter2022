grade = input("Please enter score")

def computegrade():

    try :
        score = float(grade)
    except :
        print ("Bad Score")
        quit()

    if score < 0.0 :
        score = print ("Bad Score")

    elif score > 1.0 :
        score = print ("Bad Score")

    elif score >= 0.9 :
        score = print ("Grade: A")

    elif score >= 0.8 :
        score = print ("Grade: B")

    elif score >= 0.7 :
        score = print ("Grade: C")

    elif score >= 0.6 :
        score = print ("Grade: D")

    elif score < 0.6 :
        score = print ("Grade: F")

    return(score)

computegrade()
