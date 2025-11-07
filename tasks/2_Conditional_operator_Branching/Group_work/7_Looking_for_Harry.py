#-----Looking for Harry------


#-----Ron Weasley hasn't seen Harry in a long time. He's been searching for him for weeks, searching every street and neighborhood. Let's help find Harry.

# Input Format
# A string is entered.

# Output Format
# Print the string "Harry is found" (without quotes) if the input string contains Harry's name; otherwise, print "Harry is lost."



#===========================================================================================
#==============SOLUTION=============

text = input("")
word = "Harry"
if word in text:
    print("Harry is found")
else:
    print("Harry is lost")