#OOPS : Encapsulation

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):  # Getter method
        return self.__balance

# Create a BankAccount instance
account = BankAccount()
account.deposit(1000)
account.withdraw(500)

# Access the balance through the getter method
print("Balance:", account.get_balance())
