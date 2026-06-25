from pip import __main__


def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter Amount to be deposited: "))

    if amount < 0:
        print("That not valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
            case _:
                print("************")
                print("Wrong Choice")
                print("************")

    print("Thank You For Using Banking Program\n"
          "Have a nice Day")

if __main__ == '__main__':
    main()