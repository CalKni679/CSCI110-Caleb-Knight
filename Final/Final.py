#Write program and programmer information as comments at the top of the script. 
#----------------------------|
#Caleb Knight                |
#CSCI110                     |
#Final                       |
#----------------------------|
import sys
import random
#Your program must read and write to a text file. The file can be used to store data for the program. 
"""A simple txt file that will display a how to play guide when selecting option 2"""
f = open("How To Play.txt", "r")
How2Play = f.read()
f.close()
#The game must be broken into several functions, preferably some fruitful functions that can be unit-tested. 
def Number_Guess_Menu():
        """What the player will see when they first start the program"""
        print("##Welcome To Number Guesser##")
        print("1.Begin Guessing")
        print("2.How To Play")
        print("3.Exit")

def Guess_Dif_Menu():
        """Lets player know what their odds are."""
        print("##Pick Your Difficulty##")
        print("1.====Easy==== (10% chance of getting it first try.)")
        print("2.===Medium=== (5%  chance of getting it first try.)")
        print("3.=Impossible= (1%  chance of getting it first try.)")

def Guessing_Difficulty():
       """Gives player option for what difficulty they would want to play at"""
       """Depending on what difficulty the player will get a different range of numbers"""
       dif_ch = input("Choose a number: ")
       rng = random.Random()
       if dif_ch == "1":
              dice_throw = rng.randrange(1, 11)
              print ("Choose between 1-10")    
              return dice_throw
       elif dif_ch == "2":
              dice_throw = rng.randrange(1, 21)   
              print ("Choose between 1-20") 
              return dice_throw       
       elif dif_ch == "3":
              dice_throw = rng.randrange(1, 101)  
              print ("Choose between 1-100") 
              return dice_throw
       else:
        print("Please make sure you are selecting between 1-3.")



def Guessing_Difficulty_Result():
    dice_throw = Guessing_Difficulty()
    """Checks the players choice, if the guess matches the guess, you win! If its too high or too low you will be told."""
    
    while True:
        try:
         num_choice = int(input("Guess A Number: "))
        
         if num_choice == dice_throw:
           print("That's Right! You Win!")
           print("The number was:", dice_throw)
         #"""Writes to a txt file"""#
           win = open("You Won!.txt", "w")
           win.write("You Won!\n")
           win.write("Print this out to hang on your fridge")
           win.close()
        #"""Allows player to keep playing until they want to quit"""
           Menu_Options()
           break      
         elif num_choice < dice_throw:
           print("Too Low! Keep Guessing!")
         elif num_choice > dice_throw:
           print("Too High! Keep Guessing!")
    
        except:
         print("Not a valid guess.")

def Menu_Options():
        """What the menu is doing behind the scenes"""
        Number_Guess_Menu()

        MChoice = input("Choose between 1-3: ")
        if MChoice == "1":
                Guess_Dif_Menu()
                Guessing_Difficulty_Result()
        elif MChoice == "2":
                print(How2Play)
        elif MChoice== "3":
                print("Good Bye")           
        else:
                print("Please make sure you are selecting between 1-3.")
                Menu_Options()
                MChoice = input("Choose between 1-3: ")
#Unit testing

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} Pass.".format(linenum)
    else:
        msg = ("Test at line {0} Fail.".format(linenum))
    print(msg)

#Unit test for making sure the range of numbers is correct for selected difficulty#
rng = random.Random()
#This one passes because the selected number is between the options of 1-10
easy_dif = rng.randrange(1, 11)
test(1 <= 7 <= 10)
#This one is a fail due to being outside the range of the available options
easy_dif = rng.randrange(1, 11)
test(1 <= 15 <= 10)




Menu_Options()
