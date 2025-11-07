#-----Вор и ворон------

#-----A line is entered. If the line contains a thief (Thief) and no raven, call the police (enter Police!). If there is a raven, talk to it and enter Car!
# If there is nothing like that, do not enter anything.





#===========================================================================================
#==============SOLUTION=============

word = input("")

if "ворон" in word:
    print("Кар!")
elif "Вор" in word or "вор" in word and "ворона" not in word:
    print("Полиция!")