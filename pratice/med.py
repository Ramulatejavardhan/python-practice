class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
account1 = BankAccount("Rahul", 5000)
account1.deposit(1000)