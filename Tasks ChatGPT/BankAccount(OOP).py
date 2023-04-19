'''Разработайте класс BankAccount, который будет представлять банковский счет.
 Каждый объект этого класса должен иметь уникальный номер, имя владельца, текущий баланс и процентную ставку.
 Класс должен иметь методы для пополнения баланса, снятия денег со счета,
 проверки баланса и начисления процентов на остаток на конец месяца.

Класс должен содержать атрибут класса total_accounts,
 который будет хранить количество созданных объектов этого класса.
 Также класс должен иметь метод класса display_total_accounts(),
 который будет выводить в консоль общее количество созданных банковских счетов.

Ваш класс BankAccount должен использовать все принципы ООП, включая наследование,
инкапсуляцию и полиморфизм.'''


class BankAccount:
    total_accounts = 0

    def __init__(self, account_id, owner, balance, interest_rate):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Error')
        else:
            self.balance -= amount

    def get_balance(self):
        print(self.balance)

    @classmethod
    def display_total_accounts(cls):
        """Вывести общее количество созданных банковских счетов"""
        print(cls.total_accounts)


class SavingsAccount(BankAccount):
    def __init__(self, account_id, owner, balance, interest_rate, month):
        super().__init__(account_id, owner, balance,interest_rate)
        self.month = month

    def calculate_interest(self):
        r = (self.interest_rate/100) / 12
        return self.balance*(1 + r) ** self.month


