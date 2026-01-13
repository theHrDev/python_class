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
    
    
#input("Enter your name: ")

# age = int(input("Enter your age: "))

# if( age > 18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")
    
# print("Good")


# if(age < 18):
#     print("you are not eligible to vote")
# else:
#     print("you are eligible to vote")
    
# print("Good")

# if(False):
#     print("yes")
# else:
#     print("no")

# num = 12345
# print(type(num))

# num_str = str(num)
# print(num_str)
# print(type(num_str))

# num_bool = bool(num)
# print(num_bool)
# print(type(num_bool))

# num_dec = float(num)
# print(num_dec)
# print(type(num_dec))

# logical operator (and or)
# num = 6  #assigning
# if num < 6:
#     print("num is lesser than 6")   
# elif num == 4:
#     print("num is equal to 4")
# elif num >= 4:
#     print("num is greater than or equal to 4")
# else:
#     print("num is greater than 6")
    
    
# if num == 6:
#     print("num is equal to 6")

# Login system
password = input("Enter your password: ")
username = input("Enter your user name: ")
print("Signup successfully, proceed to login")

    
repeat_username = input("Enter your username: ")
repeat_password = input("Enter your password: ")
if(repeat_password == password):
    print("Login successfully")
else:
    print("Wrong password")
    
len("word ")