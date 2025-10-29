
def addition():
    first_num = int(input("Enter first number "))
    second_num = int(input("Enter second number "))
    result = first_num + second_num
    print(result)

def substraction():
    first_num = int(input("Enter first number "))
    second_num = int(input("Enter second number "))
    result = first_num - second_num
    print(result)

def multiplication():
    first_num = int(input("Enter first number "))
    second_num = int(input("Enter second number "))
    result = first_num * second_num
    print(result)

def division():
    first_num = int(input("Enter first number "))
    second_num = int(input("Enter second number "))
    result = first_num / second_num
    print(result)



print("Welcome to my mini calculator")
def mini_calculator():
    print("What do you want to do")
    steps = input("1.Addition 2.Substraction 3.Multiplication 4.Division  ")
    if(steps == "1"):
        addition()
    elif(steps == "2"):
        substraction()
    elif(steps == "3"):
        multiplication()
    elif(steps == "4"):
        division()
    else:
        print("Function not included")
    print("Do you want to do something else")
    steppps = input("y.yes  n. no ")
    if(steppps == "y"):
        mini_calculator()
    else:
        print("Finished")

mini_calculator()



