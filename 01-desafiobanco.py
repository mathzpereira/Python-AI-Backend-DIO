menu = """
Welcome to the menu!
Please choose an option:
[a] Deposit
[b] Withdraw
[c] Balance
[d] Exit"""
balance = 0
withdrawal_count = 0

while True:

    print(menu)
    option = input()
    if option == 'a':
        print("Operation : Deposit")
        deposit = float(input("Please inform the value you want to deposit (R$): "))
        if deposit < 0:
            print("Value not valid. Deposit cancelled.")
        else:
            balance += deposit
            print(f"Deposit of R$ {deposit:.2f} completed with success.")
        
    elif option == 'b':
        print("Operation : Withdraw")
        withdraw = float(input("Please inform the value you want to withdraw (R$): "))
        if balance < 0:
            print("Your balance is empty.")
        elif withdraw < 0:
            print("Value not valid. Withdrawal cancelled.")
        elif withdraw > 500:
            print("Value not allowed. The maximum amount of a withdrawal is R$ 500.00")
        elif withdrawal_count >= 3:
            print("You reached the maximum amount of withdrawals today. Come back tomorrow!")
        else:
            balance -= withdraw
            withdrawal_count+=1
            print(f"Withdrawal of R$ {withdraw:.2f} completed with success.")

    elif option == 'c':
        print("Operation : Balance")
        print(f"Your current balance is: R$ {balance:.2f}. You still have {3-withdrawal_count} withdraw(s) for today.")

    elif option == 'd':
        break

