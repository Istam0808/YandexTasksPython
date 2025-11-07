#-----Robot in the library------


#-----A robot has appeared in the school library to organize the shelves. The robot's task is to place books with the same title next to each other on the shelf. Two strings of book titles are entered. Write a program that will determine whether the books are identical.

# If the entered strings are the same, output:

# Identical books.

# Otherwise:

# Various books.


#===========================================================================================
#==============SOLUTION=============


b1 = input("")
b2 = input("")
if b1 == b2:
    print("Identical books.")
else:
    print("Various books.")
    