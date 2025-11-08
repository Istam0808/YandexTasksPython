# Напишите программу, которая считывает с клавиатуры одно за другим два дробных числа, а затем строку. Если эта строка является обозначением одной из четырёх основных математических операций (+, -, * или /), то выведите результат применения этой операции к введенным ранее числам, в противном случае выведите «888888». Также «888888» следует вывести, если пользователь захочет поделить на ноль.

first_number = float(input())
second_number = float(input())
operation = input()

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number == 0:
        print("888888")
    else:
        print(first_number / second_number)
else:
    print("888888")
