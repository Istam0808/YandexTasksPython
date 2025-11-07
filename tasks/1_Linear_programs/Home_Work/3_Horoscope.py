#-----Horoscope------


#-----We have a business plan!

# First item: write a horoscope program that, based on a few simple questions, produces a strictly individual analysis of personality traits. We will do this using cutting-edge astrological techniques. Write a program that reads from the keyboard, in the following order: first name, last name, favorite animal, zodiac sign.

# After that the program outputs:

# Individual horoscope for the user [first name] [last name]
# In a previous life you were: [favorite animal]
# Your zodiac sign - [zodiac sign] , you have a sensitive nature.

# Note: the sentence about a sensitive nature is always printed, regardless of what the user entered (this is a parody of the process of creating a "real" horoscope). The same fixed text inserts the words provided by the user.

# Of course, a space before a comma is not correct according to the rules, but let it stay here.



#===========================================================================================
#==============SOLUTION=============

name = input()
surname = input()
animal = input()
zodiac = input()

print(f"Individual horoscope for the user {name} {surname}")
print(f"In a previous life you were: {animal}")
print(f"Your zodiac sign - {zodiac} , you have a sensitive nature.")
