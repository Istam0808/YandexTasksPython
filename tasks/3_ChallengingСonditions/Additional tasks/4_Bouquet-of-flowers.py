# Букет цветов
# Дополнительные задачи
# макс.максимум 30 балл.30 баллов
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Букет – это как минимум три цветка. Или больше. Помогите собрать букет.

# Формат ввода
# Вводится 4 строки. В первых трех названия цветов, в четвертой – цветы, которые уже есть в букете.

# Формат вывода
# Если в букете есть указанные цветы, то нужно вывести фразу в формате:

# В букете есть {Цветок_1}, {Цветок_2}, {Цветок_3}.

# Или только те, что есть, в порядке ввода.

# Если ни одного из них нет, вывести фразу:

# Таких цветов в букете нет.


#===========================================================================================
#==============SOLUTION=============

flower_first = input()
flower_second = input()
flower_third = input()
available_flowers = input()

result = ""

if flower_first in available_flowers:
    result = flower_first

if flower_second in available_flowers:
    if result:
        result = result + ", " + flower_second
    else:
        result = flower_second

if flower_third in available_flowers:
    if result:
        result = result + ", " + flower_third
    else:
        result = flower_third

if result:
    print("В букете есть " + result + ".")
else:
    print("Таких цветов в букете нет.")