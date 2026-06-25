# Simple ATM Simulator

balance = 1000
pin = "1234"

def check_balance():
    print("Your balance =", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")

# Login system
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            check_balance()
        elif choice == "2":
            amt = float(input("Enter amount: "))
            deposit(amt)
        elif choice == "3":
            amt = float(input("Enter amount: "))
            withdraw(amt)
        elif choice == "4":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")
else:
    print("Wrong PIN")
