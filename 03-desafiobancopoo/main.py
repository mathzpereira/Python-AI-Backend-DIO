from models import *

menu = """
Welcome to the menu!
Please choose an option:
[a] Deposit
[b] Withdraw
[c] View history
[d] Add a new client
[e] Add a new account
[f] Show client account list
[g] Show all accounts
[q] Exit"""

ROOT_PATH = Path(__file__).parent
log = open(ROOT_PATH / 'log.txt', 'a')

def main():

    while True:
        print(menu)
        option = input()

        if option == 'a':
            account_number = input('Enter the account number: ')
            value = float(input('Enter the deposit value: '))
            account = Account.find_account(account_number)
            if account:
                account.deposit(value)
            else:
                print('Account not found')

        elif option == 'b':
            account_number = input('Enter the account number: ')
            value = float(input('Enter the withdrawal value: '))
            account = Account.find_account(account_number)
            if account:
                account.withdraw(value)
            else:
                print('Account not found')

        elif option == 'c':
            account_number = input('Enter the account number: ')
            account = Account.find_account(account_number)
            if account:
                for transaction in account._history.transactions_generator():
                    print("Transaction:", transaction['type'], "| Value: R$", transaction['value'], "| Date:", transaction['date'], "\n")
            else:
                print('Account not found')

        elif option == 'd':
            name = input('Enter the name: ')
            cpf = input('Enter the CPF: ')
            address = input('Enter the address: ')
            birthdate = input('Enter the birthdate: ')
            individual = Individual(address=address, cpf=cpf, name=name, birth_date=birthdate)
            print(f'Client {individual._name} added with success!')

        elif option == 'e':
            client_cpf = input('Enter the client CPF: ')
            client = Individual.find_client(client_cpf)
            if client:
                account_number = input('Enter the account number: ')
                account = Account.find_account(account_number)
                if account:
                    print('Account already exists')
                else:
                    account = Account.new_account(client, account_number)
                    client.add_account(account)
                    print('Account created successfully')
            else:
                print('Client not found')

        elif option == 'f':
            client_cpf = input('Enter the client CPF: ')
            client = Individual.find_client(client_cpf)
            if client:
                print(f'Client {client._name} has the following accounts:')
                for account in client._accounts:
                    print(account._number)
            else:
                print('Client not found')

        elif option == 'g':
            for acc in AccountIterator():
                print("Account number:", acc._number, "| Balance: R$", acc._balance, "| Client:", acc._client._name, "\n")

        elif option == 'q':
            break

        else:
            print('Invalid option')

def user():
    user = Individual("Rua dos Bobos", "123", "Fulano", "01/01/2000")
    account = Account.new_account(user, "22")
    user.add_account(account)

user()
main()
