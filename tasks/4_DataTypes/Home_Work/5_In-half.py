# Write a program that reads a single integer from the keyboard and prints "even" or "odd" 
# depending on whether the number is even or odd.

# Hint: Remember the // and %.

number = int(input())

if number % 2 == 0:
    print("even")
else:
    print("odd")