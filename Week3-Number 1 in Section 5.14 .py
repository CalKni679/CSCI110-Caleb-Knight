#------------------------|
#Caleb Knight            |
#CSCI110                 |
#Number 1 in Section 5.14|
#------------------------|

def days_in_week (day_number):
    if day_number == 0:
        print ("Sunday")
        print ("Months that begin on a Sunday always have a Friday the 13th in them.")
    elif day_number == 1:
        print ("Monday")
        print ("It’s a universally recognized fact that Mondays suck.")
    elif day_number == 2:
        print ("Tuesday")
        print ("Uranus was first discovered on a Tuesday by William Herschel on March 13, 1781.")
    elif day_number == 3:
        print ("Wednesday")
        print ("Also known as humpday")
    elif day_number == 4:
        print ("Thursday")
        print ("Thursday is named after Thor, the Norse god of thunder, lightning, and storms.")
    elif day_number == 5:
        print ("Friday")
        print ("A popular American acronym is “TGIF,” which means “Thank God It’s Friday.")
    elif day_number == 6:
        print ("Saturday")
        print ("Saturday takes its name from Saturn, the Roman god of generation, dissolution, plenty, wealth, agriculture, periodic renewal, and liberation.")

    else:
     print("Invalid choice.")


#Insert day number here#
#Pick a number between 0-6#
#Any number outside of 0-6 will result in invalid choice.#
days_in_week(0)


