#-----Chrismas tree-3------

#-----Add to the previous program the ability to enter "once" instead of "one".





#===========================================================================================
#==============SOLUTION=============

first = input()
second = input()
third = input()

words_ok = (first == "one" or first == "once") and second == "two" and third == "three"
digits_ok = first == "1" and second == "2" and third == "3"

if words_ok or digits_ok:
    print("BURN")
else:
    print("DON'T BURN")