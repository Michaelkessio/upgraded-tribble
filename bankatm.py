class PeoplesBank:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."


class ThePeoplesBankATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, initial_balance=0):
        if account_number not in self.accounts:
            account = PeoplesBank(account_number, pin, initial_balance)
            self.accounts[account_number] = account
            return "Account created successfully."
        else:
            return "Account already exists."

    def login(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return self.accounts[account_number]
        else:
            return None


def main():
    atm = ThePeoplesBankATM()

    while True:
        print("\nWelcome to The Peoples Bank ATM!")
        print("1. Create an account")
        print("2. Login")
        print("3. Quit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            initial_balance = float(input("Enter initial balance: "))
            result = atm.create_account(account_number, pin, initial_balance)
            print(result)
        elif choice == "2":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = atm.login(account_number, pin)
            if account:
                while True:
                    print("\nAccount Menu:")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    option = input("Select an option (1/2/3/4): ")

                    if option == "1":
                        print(f"Current Balance: ${account.check_balance()}")
                    elif option == "2":
                        amount = float(input("Enter deposit amount: "))
                        print(account.deposit(amount))
                    elif option == "3":
                        amount = float(input("Enter withdrawal amount: "))
                        print(account.withdraw(amount))
                    elif option == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Login failed. Invalid account number or PIN.")
        elif choice == "3":
            print("Goodbye!")
            print("Thank you for your business!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

