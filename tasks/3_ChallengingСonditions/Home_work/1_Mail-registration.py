#-----Mail registration------

#-----When registering a new email account, the user is usually asked to enter, among other things, a desired login, as well as a backup email address (in case they need to recover a forgotten password). Write a program that checks that the user hasn't mixed anything up and has entered a correct login (not containing the "@" symbol) and a correct backup address (containing the "@" symbol). No other checks besides those specified here need to be performed.
# Input format
# Two lines are entered: the login proposed by the user and the backup address.
# Output format
# One line is output: if all conditions are met, then "OK" is output (in Latin letters); if "@" is present in the login, then "Incorrect login" is output; if the login is correct but "@" is missing in the address, then "Incorrect address" is output.





#===========================================================================================
#==============SOLUTION=============

login = input()
backup_email = input()

if "@" in login:
    print("Некорректный логин")
elif "@" not in backup_email:
    print("Некорректный адрес")
else:
    print("OK")
