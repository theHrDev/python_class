
print("Welcome Back")
total_balance = int(input("Enter your intial balance: "))
transaction_history = {}

def deposit():
    global total_balance, transaction_history
    deposited_amount = int(input("Enter the amount you want to deposit: "))
    total_balance = total_balance + deposited_amount
    transaction_message = f"You deposited {deposited_amount} into your account"
    transaction_history["Deposit"] = [transaction_message]
    print("Amount Desposited successfully")
    print("Your balance is ")
    print(total_balance)

def withdraw():
    global total_balance, transaction_history
    withdrawn_amount = int(input("Enter the amount you want to withdraw: "))
    transaction_message = f"{withdrawn_amount} was withdrawn from  your account"
    transaction_history["Withdraw"] = [transaction_message]
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

def transaction_his():
    print("Your transaction summary; ")
    print(transaction_history)
    
    
    
def bank_transaction():
    print("What do you want to do")
    transaction = input("1. Deposit  2.Withdraw  3.Check Balance: 4. Transaction History " )
    if(transaction == "1"):
        deposit()
    elif(transaction == "2"):
        withdraw()
    elif(transaction == "3"):
        balance()
    elif(transaction == "4"):
        transaction_his()
    else:
        print("Unknown Transaction")

    print("Do you want to perform another transaction")
    another_transaction = input("y.yes  n.no : ")
    if(another_transaction == "y"):
        bank_transaction()
    else:
        print("Thanks for Banking with us")


bank_transaction()



