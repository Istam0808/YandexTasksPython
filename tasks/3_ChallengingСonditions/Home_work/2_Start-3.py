#-----Start-3------

#-----Now, to start, it's enough for three, two, one, or once to be present in the corresponding line. If the condition is met, we print START; otherwise, ERROR.





#===========================================================================================
#==============SOLUTION=============

first = input()
second = input()
third = input()

first_ok = "three" in first
second_ok = "two" in second
third_ok = "one" in third or "once" in third

if first_ok and second_ok and third_ok:
    print("START")
else:
    print("ERROR")
