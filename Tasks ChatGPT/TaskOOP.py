'''Создайте класс BankAccount (банковский счет) с атрибутами balance (баланс) и owner (владелец).
У класса должны быть методы deposit (внесение денег на счет),
 withdraw (снятие денег со счета) и get_balance (получение баланса счета).
 Методы deposit и withdraw должны проверять, что внесенные или снимаемые средства не превышают баланс на счете.

Затем создайте подкласс SavingsAccount (сберегательный счет),
который наследует атрибуты и методы родительского класса BankAccount,
но также имеет атрибут interest_rate (процентная ставка),
который используется для расчета процентов на остаток на счете.
 Метод calculate_interest должен возвращать сумму процентов, которые будут начислены на остаток на счете,
 в соответствии с заданной процентной ставкой.

Затем создайте подкласс CheckingAccount (расчетный счет),
который также наследует атрибуты и методы родительского класса BankAccount.
Добавьте метод withdraw_limit, который устанавливает лимит на сумму,
которую можно снять за один раз со счета. Метод withdraw должен проверять,
 что запрошенная сумма не превышает лимита снятия.

Наконец, создайте класс Customer (клиент),
у которого есть атрибуты name (имя) и accounts (счета),
которые хранятся в списке.
Класс должен иметь методы add_account (добавление счета)
и remove_account (удаление счета) для управления списком счетов.
Метод total_balance должен возвращать общий баланс всех счетов клиента.'''


class BankAccount:

    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > self.balance:
            return print('Error')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return print('Error')
        else:
            self.balance -= amount

    def get_balance(self):
        print(self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, interest_rate, month):
        super().__init__(balance, owner)
        self.interest_rate = interest_rate
        self.month = month

    def calculate_interest(self):
        r = (self.interest_rate/100) / 12
        self.balance *= (1 + r) ** self.month


class CheckingAccount(BankAccount):
    def __init__(self, balance, owner, withdrawal_limit):
        super().__init__(balance,owner)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded")


class Costumer:
    def __init__(self, name, accounts=[]):
        self.name = name
        self.accounts = accounts

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)


# GPT
class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > self.balance:
            print('Error')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Error')
        else:
            self.balance -= amount

    def get_balance(self):
        print(self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, balance, owner, interest_rate, month):
        super().__init__(balance, owner)
        self.interest_rate = interest_rate
        self.month = month

    def calculate_interest(self):
        r = (self.interest_rate/100) / 12
        interest = self.balance * (1 + r) ** self.month
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, balance, owner, withdrawal_limit):
        super().__init__(balance, owner)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount <= self.balance:
            super().withdraw(amount)
        else:
            print("Insufficient funds")

class Customer:
    def __init__(self, name, accounts=None):
        self.name = name
        self.accounts = accounts or []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)




