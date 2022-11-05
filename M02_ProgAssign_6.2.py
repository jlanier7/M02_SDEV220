#------------------------------------------------------------------------------------------------------------------------------------
#Program Name: Book Thing To Do 6.2
#
#Author: Josh Lanier 
#
#SDEV 220
#
#11/5/22
#
#Program Purpose: To print a descending list of integers, from 3 to 0, one at a time. 
#
#Variables: 
#   
#    -guess_me:  (integer) number that program is trying to reach through positive iteration from 1.
#  
#    -number:    (integer) while loop counter variable. This number is incremented at the bottom of the while loop and is 
#                compared to 'guess_me' through each loop until it is equal to it, and then the program prints a message and exits
#                the loop.
#------------------------------------------------------------------------------------------------------------------------------------

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:                     #number is higher than 'guess_me'
        print('oops') 
    number += 1