class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"deposited #{amount}. Current balance: #{self.balance}")
        else:
            print("Invalid amount. Enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew #{amount}. Current balance: #{self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def total_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"current balance: #{self.balance}")


c1 = BankAccount("11222", "Tune", 1000)
print(c1.balance)
print(c1.deposit(500))
print(c1.withdraw(200))
print(c1.total_balance())
