#------------------------------------------------------------------------------------------------------------------------------------
# Program Name: Book Thing To Do 6.3
#
# Author: Josh Lanier 
#
# SDEV 220
#
# 11/5/22
#
# Program Purpose: To find a number in range(10) that matches the variable 'guess_me'. 
#
# Variables: 
#   
#    -guess_me:  (integer) static number that program uses to compare 'number' against as 'number' iterates through range(10).
#  
#    -number:    (integer) 'for' loop iteration placeholder variable. This number is iterated through range(10) by the first line of the  
#                for loop and is compared to 'guess_me' through each loop until it is equal to 'guess_me', and then the program prints a 
#                message and exits the loop.
#------------------------------------------------------------------------------------------------------------------------------------

guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:                     #number is great than 'guess_me'
        print('oops')         
