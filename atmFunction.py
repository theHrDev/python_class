
print("Welcome Back")
total_balance = int(input("Enter your intial balance: "))

def deposit():
    global total_balance
    deposited_amount = int(input("Enter the amount you want to deposit: "))
    total_balance = total_balance + deposited_amount
    print("Amount Desposited successfully")
    print("Your balance is ")
    print(total_balance)

def withdraw():
    global total_balance
    withdrawn_amount = int(input("Enter the amount you want to withdraw: "))
    if(withdrawn_amount <= total_balance):
        total_balance = total_balance - withdrawn_amount
        print("Amount Withdrawn successfully")
        print("Your balance is ")
        print(total_balance)

    else:
        print("Insufficient Fund")
        print("Your balance is ")
        print(total_balance)

def balance():
    global total_balance
    print("Your balance is ")
    print(total_balance)

def bank_transaction():
    print("What do you want to do")
    transaction = input("1. Deposit  2.Withdraw  3.Check Balance:  " )
    if(transaction == "1"):
        deposit()
    elif(transaction == "2"):
        withdraw()
    elif(transaction == "3"):
        balance()
    else:
        print("Unknown Transaction")

    print("Do you want to perform another transaction")
    another_transaction = input("y.yes  n.no : ")
    if(another_transaction == "y"):
        bank_transaction()
    else:
        print("Thanks for Banking with us")


bank_transaction()



