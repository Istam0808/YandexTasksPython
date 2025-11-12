first_password = input()
second_password = input()

if len(first_password) < 8:
    print("Короткий!")
elif first_password != second_password:
    print("Различаются.")
else:
    print("OK")