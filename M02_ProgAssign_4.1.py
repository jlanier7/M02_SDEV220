#-------------------------------------------------------------------------------------------------------------------------------------
#Program Name: Book Thing To Do 4.1
#
#Author: Josh Lanier 
#
#SDEV 220
#
#11/5/22
#
#Program Purpose: The program is designed to evaluate whether a variable 'guess' is lower than, higher than, or equal to the CONSTANT 
#    'SECRET', and then print the conclusion it reaches.   
#
#Variables: 
#   
#    -SECRET: (integer constant) holds the value that variable 'guess' is being compared against to, to produce the conclusion phrase.
#  
#    -guess: (integer) holds the value that constant 'SECRET' is being compared against.
#
#-------------------------------------------------------------------------------------------------------------------------------------

SECRET = int(6)
guess = int(10)

if guess < SECRET:
    print('too low')
elif guess > SECRET:
    print('too high')
else:
    print('just right')