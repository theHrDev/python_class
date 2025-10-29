a = 2
if(a < 12):
    print("First")
elif(a < 15):
    print("second")

    # this will print first cos the condition is meant in the first instance and breaks

a = 10
if(a < 12):
    print("first")
elif(a < 20):
    print("second")

print("==========")
a = 12
if(a < 12):
    print("first")
elif(a < 20):
    print("second")
elif(a <2):
    print("Third")
if(a == 12):
    print("Forth")


# Login flow
password = input("Enter your password: ")
username = input("Enter your username: ")

print("Login Successfully")

repeated_password = input("Repeat your password: ")
repeated_username = input("Repeat your username: ")

if(password != repeated_password):
    print("Incorrect password")
elif(username != repeated_username):
    print("Incorrect username")
elif(password == repeated_password and username == repeated_username):
    print("Login Successful")