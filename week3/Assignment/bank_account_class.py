class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def display(self):
        print("Balance:", self.balance)

# Example usage
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
acc.display()
