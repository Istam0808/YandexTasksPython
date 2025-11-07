#-----Meow------


#-----Write a program that reads one line and then prints "MEOW" if the input line contains the substring "cat" and "WOOF" otherwise.



#===========================================================================================
#==============SOLUTION=============

text = input("")
word = "cat"
if word in text:
    print("MEOW")
else:
    print("WOOF")