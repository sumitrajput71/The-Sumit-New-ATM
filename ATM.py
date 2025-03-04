import os
clear = lambda: os.system('cls')

pin=1234 
print("   Welcome to ATM")
balance = 50000

def r_pin():
    n = int(input("Enter your pin : "))
    if(n==pin):
        clear()
        print("your pin is valid")
    else:
        print("your pin is invalid. So,enter pin again")
        r_pin()

def withdraw():
    global balance
    amount = int(input("Enter your amount : "))
    if(amount>=2000 and amount<=50000 and amount>=0):
        clear()
        print("your amount is valid\n")
    else:
        print("you cannot withdraw any amount less than 2000 Rs and more than  50000 Rs.so,enter your amount again")
        withdraw()
    mobile = int(input("Enter your mobile number : "))
    if(mobile==9315201192):
        clear()
        print("your mobile number is valid\n")
    else:
        print("your mobile number is wrong.so,re-start your process")
        withdraw()
    otp = int(input("Enter your OTP : "))
    if(otp == 1122):
        clear()
        print("your OTP is valid\n")
        print("Collect your Amount\nThanks for using\n")
    else:
        print("your OTP is invalid. so,re-start your process\n")
        withdraw()
    balance -= amount    
    option()
    
def change_pin():
    old_pin = int(input("Enter Old Pin : "))
    new_pin = int(input("Enter New Pin : "))

    if(old_pin == pin):
        pin == new_pin
        print("PIN successfully changed")
    else:
        print("PIN didn't match")
    option()
    
def Check_balance():
    print(f"your balance is : {balance}")
    option()
    clear()
    
def option():
    print("1. re-use ATM")
    print("2. leave")
    option = int(input("select 1 & 2 : "))

    if(option == 1):
        main()
    elif(option == 2):
       print("OK, Ram Ram ji")

def main():
    r_pin()

    print("1. withdraw")
    print("2. change pin")
    print("3. check balance")
    print("4. leave")
    option = int(input("select options : "))
    clear()

    if(option == 1):
        withdraw()
    elif(option == 2):
        change_pin()
    elif(option == 3):
        Check_balance()
    elif(option == 4):
        print("OK, Ram Ram ji")
    

main()





