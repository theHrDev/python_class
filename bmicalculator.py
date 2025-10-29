

print("Welcome to my BMI calculator, Follow the following prompt to continue")
def bmi_calculator():
    weight = int(input("Enter your weight: "))
    height = int(input("Enter your height: "))
    bmi = weight / (height * height)
    if(bmi <= 18):
        print(bmi)
        print("Underweight")
    elif(bmi <= 25):
        print(bmi)
        print("Normal Weight")
    elif(bmi <= 30):
        print(bmi)
        print("OverWeight")
    else:
        print(bmi)
        print("Obese")
    print("Do you want to calclulate again")
    another_calculation = input("1. yes 2.no ")
    if(another_calculation == "1"):
        bmi_calculator()
    else:
        print("Finished")
bmi_calculator()
        
