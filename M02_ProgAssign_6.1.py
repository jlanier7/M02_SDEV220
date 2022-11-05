#------------------------------------------------------------------------------------------------------------------------------------
#Program Name: Book Thing To Do 6.1
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
#    -numList:   (list object [int]) holds the list integers to be printed. '-1' step increment is used in range() to return  
#                descending list of integers.
#  
#    -num:       (integer) iterator placeholder for 'for' loop. Program will print each iteration in 'for' loop, working through 
#                numList list.
#
#------------------------------------------------------------------------------------------------------------------------------------

numList = list(range(3, -1, -1))

for num in numList:
    print(num)