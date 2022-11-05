#------------------------------------------------------------------------------------------------------------------------------------
#Program Name: Book Thing To Do 4.2
#
#Author: Josh Lanier 
#
#SDEV 220
#
#11/5/22
#
#Program Purpose: To allow a user to define which of four objects they are thinking of, by setting variables 'small' and 'green'
#              to True or False, and letting the program work through a decision structure to guess which object they were thinking
#              of.  
#
#Variables: 
#   
#    -small:   (Boolean data type) describes whether a referenced object is small: value is True if user is referencing a small
#              object, and False if user is referencing a large object.
#  
#    -green:   (Boolean data type) describes whether a referenced object is green: value is True if user is referencing a green
#              object, and False if user is referencing a not green object.
#
#    -choice:  (String data type) placeholder for eventual value of result of decision structure - what item the user is 
#              thinking of - to interpolate into the printed f-string at the end of the program.
#            
#------------------------------------------------------------------------------------------------------------------------------------

small = True
green = True
choice = ''

if small == True:
    if green == True:
        choice = 'pea'
    else:
        choice = 'cherry'
else:
    if green == True:
        choice = 'watermelon'
    else:
        choice = 'pumpkin'

print(f'You were thinking of a {choice}!')