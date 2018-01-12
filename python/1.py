# Import modules
import time
import os
# All accounts
f1=open("register.txt","a+")
users = {
    
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["mail"] = []
    f1.write(str(username)+" "+str(password)+"\n")
    time.sleep(1)
    print("Account has been created")

# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
     
     
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        #return session(username)
        os.system("python linkedlist.py")
    else:
        print("Invalid username or password")

# Register

print("Welcome to the system. Please register or login.")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

f1.close()
# On exit
print("Shutting down...")
time.sleep(1)
