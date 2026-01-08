class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds!")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())
