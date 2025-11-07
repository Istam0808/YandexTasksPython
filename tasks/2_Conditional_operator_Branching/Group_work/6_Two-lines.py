#-----Two lines------


#-----Write a program that creates a phrase from two input lines as follows: first, the line that comes earlier in alphabetical order is displayed, then the second line is displayed on the same line without spaces.



#===========================================================================================
#==============SOLUTION=============

first = input()
second = input()

if first <= second:
    print(first + second)
else:
    print(second + first)
