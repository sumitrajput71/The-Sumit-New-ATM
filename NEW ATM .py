import os
clear = lambda: os.system('cls')

users = []

def create_user():
    name = input("Enter Name: ")
    account_number = int(input("Enter Account number: "))
    pin = int(input("Enter PIN: "))
    amount = int(input("Enter amount: "))

    user = {"name": name, "account_number": account_number, "pin": pin, "amount": amount}
    users.append(user)

    print("Account Created Successfully")

def get_account():
    account_number = int(input("Enter account number: "))
    for i in range(len(users)):
        if(account_number == users[i]["account_number"]):
            return 0
    
    print("Account not found")
    return -1

def change_pin():
    account_index = get_account()

    if(account_index == -1):
        return

    old_pin = int(input("Enter Old PIN: "))
    new_pin = int(input("Enter New PIN: "))

    if(old_pin == users[account_index]["pin"]):
        users[account_index]["pin"] == new_pin
        print("PIN successfully changed")
    else:
        print("PIN didn't match")

def check_balance():
    account_index = get_account()

    if(account_index == -1):
        return
     
    print(f"Hi {users[account_index]["name"]}, Your current balance is: {users[account_index]["amount"]}")

def withdraw_amount():
    account_index = get_account()

    if(account_index == -1):
        return

    amount = float(input("Enter the amount of withdraw: "))

    users[account_index]["amount"] -= amount

    print("Amount withdrawn successfully")
    print(f"Hello {users[account_index]["name"]}, your current balance is {users[account_index]["amount"]}")

def deposit_amount():
    account_index = get_account()

    if(account_index == -1):
        return

    amount = float(input("Enter the amount of deposit: "))

    users[account_index]["amount"] += amount

    print("Amount deposited successfully")
    print(f"Hello {users[account_index]["name"]}, you current balance is {users[account_index]["amount"]}")

def show_all_accounts():
    for i in range(len(users)):
        print(users[i])
        print("--------------")

def main():
    print("1. Create Account")
    print("2. Change PIN")
    print("3. Withdraw Amount")
    print("4. Deposit Amount")
    print("5. Check Balance")
    print("6. Show all accounts")
    
    option = int(input("Select option: "))

    clear()
    if(option == 1):
        create_user()
    elif(option == 2):
        change_pin()
    elif(option == 3):
        withdraw_amount()
    elif(option == 4):
        deposit_amount()
    elif(option == 5):
        check_balance()
    elif(option == 6):
        show_all_accounts()
    else:
        print("Invalid option selected")

    main()


main()









# #def atm_program():
# #    balance = 5000
# balance = 5000 
# pin = 9315


# while True:
    
#     n=int(input("enter your pin\n : "))
#     if(n==pin):
#         print("\nyour pin is valid ")
#     else:
#         print("your pin is invalid")
#         break
#     print("press 1. check balance")
#     print("press 2. Deposit")
#     print("press 3. withdraw")
#     print("press 4. Exit")

#     choice = input("enter your choice(1/2/3/4):")

#     if choice =='1':
#         amount = float(input("Enter your amount\n:"))
        
#         print(f"your current balance is :{balance}")

#     elif choice =='2':
#         amount = float(input("enter the amount to Deposit: "))
#         if amount > 0:
#             balance += amount
#             print(f"deposited {amount}\nnew balance is:{balance}")
#         else:
#             print("invalid amount\nplease enter a positive number.")

#     elif choice == '3':
#         amount = float(input("enter the amount of withdraw: "))
#         if 0< amount <= balance:
#             balance -= amount
#             print(f"withdrow {amount}.new balance is:{balance}")
#         elif amount> balance:
#             print("insufficient funds.")

#         else:
#             print("invalid amount\nplease enter a positive password: ")

#     elif choice =='4':
#         print("thank you for using the ATM")
#         break 
#     else:
#         print("invalid choice\nplease enter a number between 1 to 4.")
        
            