class BankAccount():
    __balance = 0

    def deposite(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
                print('you deposited: ', amount)
            else:
                raise TypeError()
        except TypeError:
            print('invalid amount')

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError()
            elif amount <= self.__balance:
                self.__balance -= amount
            else:
                print('insufficient balance')
        except ValueError:
            print('invalid amount')

    def get_balance(self):
        print(self.__balance)

acc = BankAccount()
acc.get_balance()
acc.deposite(100)
acc.withdraw(150)
acc.get_balance()