# Вводится 3-х значное число. Нужно разделить его на отдельные цифры и с их помощью записать наименьшее возможное, но тоже трехзначное число. 
# В задаче нельзя использовать циклы, строки и списки.


# Формат ввода
# Трехзначное число.

# Формат вывода
# Минимальное число, записанное теми же цифрами

number = int(input())

hundreds = number // 100
tens = number // 10 % 10
units = number % 10

minimum = min(hundreds, tens, units)
maximum = max(hundreds, tens, units)
median = hundreds + tens + units - minimum - maximum

if minimum == 0:
    if median == 0:
        result = maximum * 100
    else:
        result = median * 100 + minimum * 10 + maximum
else:
    result = minimum * 100 + median * 10 + maximum

print(result)