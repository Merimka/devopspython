
#NOTE: Functions that are associated with classes are called methods.

# We have to create a class to represent bank account.
# functionalities for this account are:
# Initialize the bank account with an initial balance.
# Deposit a specified amount into the account.
# Withdraw a specified amount from the account,but do not allow overdrawing.
# Check the account balance.



# When we create a instance from Bank Account class, this action actually represents
# opening a new bank account.
# IN the account we have functionalities,
# like, withdrawal, deposit, check balance

class BankAccount:
    def __init__(self,initial_balance):
        self.balance = initial_balance

    def Withdraw (self,amount_to_withdraw) : 
        if amount_to_withdraw > self.balance:
            print("You cannot withdraw because there is not enough funding.") 
        elif amount_to_withdraw <= self.balance:
            print(f"You withdrew ${amount_to_withdraw}")
            self.balance -= amount_to_withdraw
            print(f"Your balance of the account is {self.balance}")


    def Deposit(self,amount_to_be_deposited):   
        self.balance += amount_to_be_deposited
        print(f"You succesfully deposit ${amount_to_be_deposited}") 
        print(f(f"Your updated balance of the account is ${self.balance}"))  


    def Check_balance(self):
        print(f"Your balance of account is ${self.balance}")  
        # Let's also return the current balance as value maybe we could latter use as
        # a variable somewhere
        return self.balance
    


# Let's create instance (object) out of this BankAccount class

#acct1 = BankAccount(60)
# You want to learn the balance of account
#acct1.Check_balance()

# I want to withdraw money from my account -> $80

#acct1.Withdraw(60)

#acct1.Check_balance()  

# Let's deposit money in to account

#acct1.Deposit(2000)

initial_balance = int(input("Welcome to our bank to create an account please enter initial deposit"))

acct = BankAccount(initial_balance)
print("Your account has been succesfully created.")
acct.Check_balance()

print("To withdraw press 1, press 2 for deposit")
user_choice = input()
if user_choice == "1":
    withdraw_amt = int(input("Enter the amount you want to withdraw"))
    acct.Withdraw(withdraw_amt)
elif user_choice == "2":
    deposit_amt = int(input("Enter the amount you want to deposit"))
    acct.Deposit(deposit_amt)
else:
    print("Invalid option.")































