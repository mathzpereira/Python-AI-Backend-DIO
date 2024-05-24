from abc import ABC, abstractmethod
from datetime import datetime

def log_decorator(func):
        def wrapper(*args, **kwargs):
            
            result = func(*args, **kwargs)
            
            print("Transaction registered. Type:", result.__class__.__name__, "| Date:", datetime.now().strftime('%d-%m-%Y %H:%M:%S'), "\n")
            
            return result
        
        return wrapper

class Account:
    _accounts = []

    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()
        self._accounts.append(self)

    def get_balance(self):
        return self._balance

    @classmethod
    @log_decorator
    def new_account(cls, client, number):
        return cls(number, client)
    
    def withdraw(self, value):
        if self._balance < value:
            print('Insufficient funds')
            return False
        elif value > 0:
            self._balance -= value
            self._history.add_transaction(Withdrawal(value))
            print(f'Withdrawal: {value}')
            return True
        else:
            print('Invalid value')
            return False
        
    def deposit(self, value):
        if value > 0:
            self._balance += value
            self._history.add_transaction(Deposit(value))
            print(f'Deposit: {value}')
        else:
            print('Invalid value')

    @classmethod
    def find_account(cls, number):
        for account in cls._accounts:
            if account._number == number:
                return account
        return None
        
class CurrentAccount(Account):
    def __init__(self, number, client, limit=500, withdrawal_limit=3):
        super().__init__(number, client)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit

    def withdraw(self, value):
        withdrawal_count = len(
            [transaction for transaction in self._history if transaction]
            )


class History():
    def __init__(self):
        self._transactions = []
    
    @log_decorator
    def add_transaction(self, transaction):
        self._transactions.append(
            {
                'type': transaction.__class__.__name__,
                'value': transaction._value,
                'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                }
        )
        return transaction
        
    def show_history(self):
        for transaction in self._transactions:
            print("Transaction:", transaction['type'], "| Value: R$", transaction['value'], "| Date:", transaction['date'], "\n")

    def transactions_generator(self):
        _history = self._transactions
        filter = input("Enter the transaction type (D= Deposit/ W= Withdrawal/ A= Any): ")
        if filter == 'D':
            _history = [transaction for transaction in self._transactions if transaction['type'] == "Deposit"]
        elif filter == 'W':
            _history = [transaction for transaction in self._transactions if transaction['type'] == "Withdrawal"]
        elif filter == 'A':
            pass
        for transaction in _history:
            yield transaction

class Transaction(ABC):
    @abstractmethod
    def register(self, account):
        pass

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    def register(self, account):
        success = account.deposit(self._value)
        if success:
            account._history.add_transaction(self)

    def __str__(self):
        return f'Deposit: {self._value}'

class Withdrawal(Transaction):
    def __init__(self, value):
        self._value = value

    def register(self, account):
        success = account.withdraw(self._value)
        if success:
            account._history.add_transaction(self)

    def __str__(self):
        return f'Withdrawal: {self._value}'

class Client:
    _clients = []

    def __init__(self, address):
        self._address = address
        self._accounts = []
        self._clients.append(self)

    def add_account(self, account):
        self._accounts.append(account)

class Individual(Client):
    def __init__(self, address, cpf, name, birth_date):
        super().__init__(address)
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date

    @classmethod
    def find_client(cls, cpf):
        for client in cls._clients:
            if client._cpf == cpf:
                return client
        return None
    
class AccountIterator():
    def __init__(self):
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(Account._accounts):
            account = Account._accounts[self._index]
            self._index += 1
            return account
        raise StopIteration