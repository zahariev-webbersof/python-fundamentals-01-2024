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
```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        # ✳️ Write code to initialize the account number and balance attributes
        
    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        # ✳️ Write code to add the deposited amount to the balance
        
    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        # ✳️ Write code to check if there are sufficient funds and deduct the withdrawn amount from the balance
        
    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        # ✳️ Write code to return the current balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        # ✳️ Call the superclass constructor to initialize common attributes
        # ✳️ Initialize the interest rate attribute
        
    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        # ✳️ Write code to calculate the interest based on the current balance and interest rate
        # ✳️ Write code to add the calculated interest to the account balance


# Testing the functionality of the classes
if __name__ == "__main__":
    # ✳️ Create a BankAccount instance with account number "123456789" and initial balance of 1000
    
    # ✳️ Deposit 500 into the account
    
    # ✳️ Withdraw 200 from the account
    
    # ✳️ Get the current balance of the bank account
    
    # ✳️ Create a SavingsAccount instance with account number "987654321", initial balance of 2000, and interest rate of 5%
    
    # ✳️ Deposit 1000 into the savings account
    
    # ✳️ Calculate and add interest to the savings account
    
    # ✳️ Get the current balance of the savings account after adding interest

```
