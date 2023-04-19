'''Напишите класс BankAccount, у которого есть атрибуты счета (account) и баланса (balance),
 а также методы для пополнения (deposit) и снятия (withdraw) денег со счета.
 Напишите метод класса from_input_string, который принимает строку в формате "account,balance"
 и создает новый объект BankAccount с заданным номером счета и балансом.
 Используйте декоратор @classmethod для создания метода from_input_string.'''


class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Error')
        else:
            self.balance -= amount

    @classmethod
    def from_input_string(cls, input_string):
        st = input_string.split(',')
        return cls(account=st[0], balance=st[1])

account1 = BankAccount("1234", 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1.balance) # выводит 1300

account2 = BankAccount.from_input_string("5678,750")
print(account2.account) # выводит "5678"
print(account2.balance) # выводит 750