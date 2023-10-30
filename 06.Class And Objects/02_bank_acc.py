#Problem : Bank Account: Create a BankAccount class with methods for deposit, withdrawal, and checking the balance.

class BankAccount :
    def __init__(self,cu_name,amount=0):
        self.cu_name = cu_name
        self.amount = amount

    def deposit(self,amount):
        if amount > 0 :
            self.amount = self.amount + amount 
            return("Successfully Deposited : %d" % self.amount)
        else:
            return("Invalid transaction!!!")

    def withdrawn(self,amount):
        if amount > 0 :
            if self.amount >= amount:
                self.amount = self.amount - amount 
                return("Successfully Widthdrawn : %d" % self.amount)
            else:
                return "insufficient fund!!!"
        else:
            return("Invalid transaction!!!")

    def get_balance(self):
        print("Total Balance : %d" % self.amount)

cust1 = BankAccount("Harshatha")
cust1.get_balance()
print(cust1.deposit(100))
cust1.get_balance()
print(cust1.withdrawn(10))
cust1.get_balance()
