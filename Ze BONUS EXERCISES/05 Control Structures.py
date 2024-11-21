'''
Control Structures:
Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien's color is green. If it is, print a message
that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)
'''
#setting variables
Alien_Color = 'green'

#using if statement to test the color 
if Alien_Color == 'green':
    print("GOOD JOB YOU EARNED 5 POINTS!")


#reusing the variable by overwriting the variable
Alien_Color = 'yellow'
#same code
if Alien_Color == 'green':
    print("GOOD JOB YOU EARNED 5 POINTS!")

