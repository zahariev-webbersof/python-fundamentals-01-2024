# Basic Bank Account Management System 🐍

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

### ✳️ Description:
1. Create a BankAccount class with the following attributes and methods:
   - Attributes:
      - account_number: A unique identifier for each bank account.
      - balance: The current balance of the bank account.
        
   - Methods:
      -__init__(): Constructor method to initialize the account number and balance.
      - deposit(amount): Method to deposit money into the account.
      - withdraw(amount): Method to withdraw money from the account.
      - get_balance(): Method to retrieve the current balance.

2. Implement a SavingsAccount class that inherits from the BankAccount class, with an additional attribute:
   - Attributes:
       - interest_rate: The interest rate for the savings account.
         
   - Methods:
       - calculate_interest(): Method to calculate and add interest to the account balance.
    
### ✳️ Tasks:
1. Create a BankAccount class with the specified attributes and methods.
2. Implement the deposit(), withdraw(), and get_balance() methods for the BankAccount class.
3. Create a SavingsAccount class that inherits from BankAccount and includes the interest_rate attribute and calculate_interest() method.
4. Test the functionality of both classes by creating instances of BankAccount and SavingsAccount and performing deposit, withdrawal, and interest calculation operations.


### Now, let's write the code for this project:
```python4
class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest


# Testing the functionality of the classes
if __name__ == "__main__":
    # Create a BankAccount instance
    account1 = BankAccount("123456789", 1000)
    
    # Deposit money into the account
    account1.deposit(500)
    
    # Withdraw money from the account
    account1.withdraw(200)
    
    # Get the current balance
    print("Bank Account Balance:", account1.get_balance())
    
    # Create a SavingsAccount instance
    savings_account1 = SavingsAccount("987654321", 2000, 5)
    
    # Deposit money into the savings account
    savings_account1.deposit(1000)
    
    # Calculate and add interest to the savings account
    savings_account1.calculate_interest()
    
    # Get the current balance of the savings account
    print("Savings Account Balance (with interest):", savings_account1.get_balance())

```
