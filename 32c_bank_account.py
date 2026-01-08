class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds!")


account = BankAccount(1000)
print(account.balance)

account.deposit(500)
account.withdraw(200)
print(account.balance)
