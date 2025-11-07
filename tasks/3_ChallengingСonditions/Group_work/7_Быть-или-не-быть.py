#-----Быть-или-не-быть------

#-----Write an oracle program. If both input lines say "To be" or both say "Not to be," then output "Choice made!"; if one says "To be" and the other "Not to be," then output "That is the question!"
# Otherwise, output "Make up your mind!"




#===========================================================================================
#==============SOLUTION=============

first = input()
second = input()

both_being = first == "Быть" and second == "Быть"
both_not_being = first == "Не быть" and second == "Не быть"
mixed = (first == "Быть" and second == "Не быть") or (first == "Не быть" and second == "Быть")

if both_being or both_not_being:
    print("Выбор сделан!")
elif mixed:
    print("Вот в чём вопрос!")
else:
    print("Определитесь!")
