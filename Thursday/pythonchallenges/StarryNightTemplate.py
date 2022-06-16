#import everything * from turtle library
from turtle import *
#important randint from random library
#from  import 


#Page Setup- fix the size of the page, 800 pixels width, 500 pixles high
#setup(,)
#Speed of the turtle drawing needs to be 0- which is the fastest speed
#speed()
#choose the night sky color


#White Moon
penup()
goto(-100,50)
pendown()
color("blue")
begin_fill()
circle(50)
end_fill()

#Makes a Cresent Moon: draws another black circle to the side of the moon.
penup()
goto(-80,50)
pendown()
color("black")
begin_fill()
circle(50)
end_fill()

#Create a function to draw one star
#A function allows you to draw a star multiple times with the function, rather than
#rewriting the code over and over.
def stars():
#    
#    
    #for i in range():
        forward(10)
        #right( )
    end_fill()

#Draw multiple stars at random (x,y) locations on the screen using loop.
#To add more or less stars change the 50 in the first line of the loop
#for i in range( ):
    #we choose -400,400 because the distance between these two values is 800 which is the screen size
    #x=randint( , )
    #same reason for -250,250 as the height of the screen is 500
    #y=randint(  ,  )
    #call the function for the stars
#   
#
#
    
#You can change simple things in your code by changing colors or values.
    #Our moon didn't show up because we had it set in the original 800x500 window
    #If you make a mistake in your code Thonny will help you find where you went wrong. Let's say we forgot the : on our function for the stars.


