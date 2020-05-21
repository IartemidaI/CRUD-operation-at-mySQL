def register(mydb, mycursor):
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    val = (username, email, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    print("Added user into database ================>")


def login(mycursor):
    username = input("Enter username: ")
    password = input("Enter password: ")
    mycursor.execute("SELECT username, password FROM users WHERE username='" +
                     username + "'")
    myresult = mycursor.fetchone()
    print("Rezult of database: ", myresult)
    if myresult == None:
        print("Login or password incorect!\n")
    elif myresult[1] != password:
        print("Login or password incorect!\n")
    else:
        print("login success!\n")


def delete(mydb, mycursor):
    username = input("Enter username to delete: ")
    mycursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = mycursor.fetchone()
    if myresult == None:
        print("Username to delete incorrect!\n")
    else:
        print("User deleted: ", myresult)
        mycursor.execute("DELETE FROM users WHERE username='" + username + "'")
        mydb.commit()


def edit(mydb, mycursor):
    username = input("Enter username to update: ")
    mycursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = mycursor.fetchone()
    if myresult == None:
        print("Username to update incorrect!\n")
    else:
        exit = False
        while not exit:
            choice = int(
                input(
                    "1. Change username\n2. Change password\n3. Change email\n0. exit\n=> "
                ))
            if choice == 1:
                new_username = input("enter new username: ")
                mycursor.execute("UPDATE users SET username='" + new_username +
                                 "' WHERE username='" + username + "'")
                username = new_username
            elif choice == 2:
                new_password = input("Enter new password: ")
                mycursor.execute("UPDATE users SET password='" + new_password +
                                 "' WHERE username='" + username + "'")
            elif choice == 3:
                new_email = input("enter new email: ")
                mycursor.execute("UPDATE users SET email='" + new_email +
                                 "' WHERE username='" + username + "'")
            elif choice == 0:
                print("Exit")
                exit = True
            else:
                print("Enter wrong number")
            mydb.commit()
            print("User updated!\n")


def show_all(mycursor):
    mycursor.execute("SELECT id, username, email FROM users")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)


def search(mycursor):
    choice = int(input("1. Find username\n2. find email\n=> "))
    if choice == 1:
        username = input("Input username: ")
        mycursor.execute(
            "SELECT id, username, email FROM users WHERE username='" +
            username + "'")
        myresult = mycursor.fetchone()
    elif choice == 2:
        email = input("Input email: ")
        mycursor.execute(
            "SELECT id, username, email FROM users WHERE email='" + email +
            "'")
        myresult = mycursor.fetchone()
    else:
        print("R.T.F.M")
    if myresult == None:
        print("Username or email not found!\n")
    else:
        print("User found! Some info about = > ", myresult)
