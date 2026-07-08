#-----------------------|
#Caleb Knight           |
#CSCI110                |
#Problem 19.6 Problem 1 |
#-----------------------|


def readposint():
    while True:
     try:
        number = int(input("Please enter a positive number: "))
        if number <= 0:    
           my_error = ValueError("{0} is not a valid number".format(number))
           raise my_error
        print("That is a positive number!")
        return number
     except:
        print("That's not a positive number")

readposint()


