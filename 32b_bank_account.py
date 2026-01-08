class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds!")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance, interest_rate):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


account = SavingsAccount(1000, 0.05)
account.apply_interest()
print(account.get_balance())
