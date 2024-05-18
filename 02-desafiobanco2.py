menu = """
Welcome to the menu!
Please choose an option:
[a] Deposit
[b] Withdraw
[c] Balance
[d] Add a new user
[e] Add a new account
[f] Show user account list
[z] Exit"""

def deposit_menu(deposit, balance, *args):
    
    if deposit < 0:
        print("Value not valid. Deposit cancelled.")
    else:
        balance += deposit
        print(f"Deposit of R$ {deposit:.2f} completed with success.")
    
    return balance

def withdraw_menu(withdraw, withdrawal_count, balance, **kwargs):
    if balance < 0:
        print("Your balance is empty.")
    elif withdraw < 0 or balance - withdraw < 0:
        print("Value not valid. Withdrawal cancelled.")
    elif withdraw > 500:
        print("Value not allowed. The maximum amount of a withdrawal is R$ 500.00")
    elif withdrawal_count >= 3:
        print("You reached the maximum amount of withdrawals today. Come back tomorrow!")
    else:
        balance -= withdraw
        withdrawal_count+=1
        print(f"Withdrawal of R$ {withdraw:.2f} completed with success.")
    
    return balance, withdrawal_count

def balance_menu(balance, withdrawal_count):
    print("Operation : Balance")
    print(f"Your current balance is: R$ {balance:.2f}. You still have {3-withdrawal_count} withdraw(s) for today.")

def add_user(user, user_list):
    user_list.append(user)

def filter_user(cpf, user_list):
    filtered_users = [user for user in user_list if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

def add_account(agency, account_number, user_list):
    cpf = input("Please inform the CPF of the account you want to add: ")
    user = filter_user(cpf, user_list)
    if user:
        account = {"agency": agency, "account_number": account_number, "user": user}
        account_number += 1
        return account, account_number
    
    print("User not found. Account cannot be created.")

def main():
    AGENCY = "0001"

    balance = 0
    withdrawal_count = 0
    user_list = []
    account_list = []
    account_number = 1
    while True:

        print(menu)
        option = input()
        if option == 'a':
            print("Operation : Deposit")
            deposit = float(input("Please inform the value you want to deposit (R$): "))
            balance = deposit_menu(deposit, balance)

        elif option == 'b':
            print("Operation : Withdraw")
            withdraw = float(input("Please inform the value you want to withdraw (R$): "))
            balance, withdrawal_count = withdraw_menu(withdraw=withdraw, withdrawal_count=withdrawal_count, balance=balance)

        elif option == 'c':
            balance_menu(balance, withdrawal_count)

        elif option == 'd':
            print("Operation: Add a new user")
            name = input("Name: ")
            birth_date = input("Date of Birth: ")
            cpf = input("CPF: ")
            print("Address: ")
            street = input("Street: ")
            number = input("Number: ")
            neighborhood = input("Neighborhood: ")
            city = input("City: ")
            state = input("State: ")
            address = street + ", " + number + " - " + neighborhood + " - " + city + "/" + state
            user = {"name": name, "birth_date": birth_date, "cpf": cpf, "address": address}
            add_user(user, user_list)

        elif option == 'e':
            account, account_number = add_account(AGENCY, account_number, user_list)
            if account:
                account_list.append(account)

        elif option == 'f':
            print("----- LIST OF ACCOUNTS -----")
            for account in account_list:
                print(f"\nAgency: {account['agency']}")
                print(f"Account Number: {account['account_number']}")
                print(f"User's CPF: {account['user']['cpf']}")

        elif option == 'z':
            break

main()
