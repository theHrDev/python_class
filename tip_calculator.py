# TIP CALCULATOR
def tip_calculator():
    print("Welcome to my Tip Calculator")

    product_price = int(input("Enter the price of the purchased products: "))
    percentage = int(input("Enter the percentage of the tips: "))
    amount_percentange = float(product_price * (percentage/100))
    amount_tobe_paid =  product_price + amount_percentange
    print("The amount you'll pay is", amount_tobe_paid)

    reloaded = input("Do you want to go again, y.yes, n.no : ")
    if(reloaded == "y"):
        tip_calculator()
    else:
        print("Thanks")

tip_calculator()