import mysql.connector
from nslogin import register, login, delete, edit, show_all, search
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="",
                               database="loginsystem")
mycursor = mydb.cursor()


def menu():
    exit = False
    while not exit:
        choice = int(
            input(
                "1. Register new user\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search user\n0. exit\n=> "
            ))
        if choice == 1:
            register(mydb, mycursor)
        elif choice == 2:
            login(mycursor)
        elif choice == 3:
            edit(mydb, mycursor)
        elif choice == 4:
            delete(mydb, mycursor)
        elif choice == 5:
            show_all(mycursor)
        elif choice == 6:
            search(mycursor)
        elif choice == 0:
            print("Exit")
            exit = True
        else:
            print("Enter wrong number")


menu()