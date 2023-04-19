'''класс BankAccountс атрибутами balance и owner. Включите методы deposit()и withdraw(),
 которые могут управлять балансом. настройка подкласса SavingsAccount,
 который будет включать проценты к балансу каждый месяц.'''


# class BankAccount:
#
#     def __init__(self, balance, owner):
#         self.balance = balance
#         self.owner = owner
#
#     def deposit(self, n):
#         return self.balance + n
#
#     def withdraw(self, n):
#         return self.balance - n
#
#
# class SavingsAccount(BankAccount):
#
#     def __init__(self, balance, owner, month):
#         self.balance = balance
#         self.owner = owner
#         self.month = month
#
#     def percent(self):
#         return self.balance(1+15/self.month)**self.month
#
# g = SavingsAccount(5000,"Peter", 12)
#
# print(g.percent())

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, months):
        super().__init__(balance, owner)
        self.months = months

    def percent(self):
        r = 0.15 / 12  # 15% годовых, переведенных в месячную ставку
        self.balance *= (1 + r) ** self.months


account = SavingsAccount(8000, 'peter', 12)

account.percent()

print(account.balance)