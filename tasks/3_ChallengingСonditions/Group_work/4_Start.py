#-----Start------

#-----Four strings are entered. If they are:

# 3
# 2
# 1
# 0

# or:

# three
# two
# one
# zero

# then you should output: START, otherwise, output ERROR.





#===========================================================================================
#==============SOLUTION=============

a = input()
b = input()
c = input()
d = input()

digits_ok = a == "3" and b == "2" and c == "1" and d == "0"
words_ok = a == "three" and b == "two" and c == "one" and d == "zero"

print("START" if digits_ok or words_ok else "ERROR")