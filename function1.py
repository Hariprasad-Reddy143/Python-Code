
#---Encapsulation------------------------------------

class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        return self.__balance 

b = Bank(1000)
b.deposit(500)
print(b.show_balance())
    
        