class BankAccount:
    def __init__(self, owner):
       self.balance = 0
       self.owner = owner

    def deposit(self, new_number) :
        self.number = new_number
        self.balance += self.number
        return self.balance

    def withdraw(self, subtract):
        self.subtract = subtract
        self.balance -= self.subtract
        return self.balance