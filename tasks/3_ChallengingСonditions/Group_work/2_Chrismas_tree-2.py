#-----Chrismas tree-2------

#-----Improve the previous program so that not only the input "one," "two," and "three" but also the input "1," "2," and "3" also output "BURN." Mixed inputs (e.g., "1," "2," and "three") output "DON'T BURN."





#===========================================================================================
#==============SOLUTION=============

first = input()
second = input()
third = input()

words_ok = first == "one" and second == "two" and third == "three"
digits_ok = first == "1" and second == "2" and third == "3"

if words_ok or digits_ok:
    print("BURN")
else:
    print("DON'T BURN")