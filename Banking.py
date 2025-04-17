class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Initialize a new bank account with an account number and an optional balance.

        Parameters:
        account_number (str): The account number of the bank account.
        balance (float): The initial balance of the account (default is 0).
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the bank account.

        Parameters:
        amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Depositing {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the bank account.

        Parameters:
        amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Error: Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawing {amount}")

    def get_balance(self):
        """
        Return the current balance of the bank account.
        """
        return self.balance

# Main program to test the BankAccount class
def main():
    # Create an instance of BankAccount
    account = BankAccount("123456789")
    
    # Test deposit and withdrawal methods
    account.deposit(5000)
    account.withdraw(2000)
    
    # Print the final balance
    print(f"Current balance: {account.get_balance()}")

# Run the main function
if __name__ == "__main__":
    main()