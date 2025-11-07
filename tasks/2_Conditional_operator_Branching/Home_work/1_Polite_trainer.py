#-----Polite trainer------


#-----Vasya noticed that when typing text, he often makes mistakes due to inattention: he skips a letter, replaces it with another, or duplicates it. He decided that he needed to practice typing text and also offer his friends such an opportunity!
# Write a program that first asks for a name, then the text that needs to be repeated with accuracy to case and punctuation marks.
# Identify yourself, please!
# {User input}
# Enter the text.
# {User input}
# Repeat the text.
# {User input}
# If the text matches the repetition, the program outputs an address by name and a message:
# {Name}, entered correctly!
# If it doesn't match:
# {Name}, it didn't work out yet, try again!





#===========================================================================================
#==============SOLUTION=============

print("Identify yourself, please!")
name = input()

print("Enter the text.")
original = input()

print("Repeat the text.")
repeat = input()

if repeat == original:
    print(f"{name}, entered correctly!")
else:
    print(f"{name}, it didn't work out yet, try again!")

