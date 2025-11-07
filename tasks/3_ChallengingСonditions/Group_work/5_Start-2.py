#-----Start-2------

#-----Now, to start, the first line can contain 3 or three, the second 2 or two, and the third 1 or one, or once. If the condition is met, we print START; otherwise, ERROR.





#===========================================================================================
#==============SOLUTION=============

a = input()
b = input()
c = input()

first_ok = a == "3" or a == "three"
second_ok = b == "2" or b == "two"
third_ok = c == "1" or c == "one" or c == "once"

print("START" if (first_ok and second_ok and third_ok) else "ERROR")