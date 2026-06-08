#-----------------------|
#Caleb Knight           |
#CSCI110                |
#Section 4.9 Problem 2 |
#-----------------------|

import turtle

#Canvas Settings
wn = turtle.Screen()        
wn.bgcolor("blue")
wn.title("Square Repeat")

#Turtle Settings
alex = turtle.Turtle()     
alex.pencolor ("orange")
alex.pensize(5)
alex.speed(0.5)
alex.hideturtle()

#Function Settings
def draw_square(t, size):
      for square_angles in range(4):
         t.forward(size)
         t.right(90)
         
#Assume the innermost square is 20 units per side
size = 20

#Used examples from sections 4.1 and 4.3 plus homework video

for repeat_square in range (6):
 draw_square(alex, size)
 size = size + 20
 
 alex.penup()
 
 alex.back(10)
 alex.left(90)
 alex.forward(10)
 alex.right(90)
 
 alex.pendown()




 


wn.mainloop()




      


