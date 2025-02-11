# AToM ATM Program
# Written by Ursula Stauber
# Handling User Input from https://www.youtube.com/watch?v=xLTCU29snoA
# Programming Fundamentals Competency 2 - Loops

# Set Global Variable
balance = float(1000.00)

# Create Negative Number Class for User Input Handling
class negative_number(Exception):
    pass

# Create Negative Balance Class for User Input Handling
class negative_balance(Exception):
    pass

# Create Not Allowed Class for User Input Handling
class not_allowed(Exception):
    pass

# Display Function
def display():
    print("\nWelcome to AToM ATM!")
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Check Balance Function
def check(balance):
    print("\nYour current balance is: ", f'{balance:.2f}')

# Deposit Function
def deposit(balance):
    # Establish Local Variable
    new_balance = balance
    looper_1 = True
    while looper_1:
        try:
            dep = float(input("\nEnter the amount to be deposited:  "))
            if dep < 0:
                raise negative_number
        except ValueError:
            print("Please enter a dollar amount.")
        except negative_number:
            print("You cannot deposit a negative amount of money.")
        else:
            new_balance = round(new_balance + dep, 2)
            print(f'{dep:.2f}', "deposited successfully.  Your new balance is: ", f'{new_balance:.2f}')
            looper_1 = False
    return new_balance

# Withdrawal Function
def withdrawal(balance):
    # Establish Local Variable
    new_balance = balance
    looper_2 = True
    while looper_2:
        try:
            wit = float(input("\nEnter the amount to be withdrawn:  "))
            if wit < 0:
                raise negative_number
            if wit > balance:
                raise negative_balance
        except ValueError:
            print("Please enter a dollar amount.")
        except negative_number:
            print("You cannot withdraw a negative amount of money.")
        except negative_balance:
            print("You have insufficient funds for this withdrawl.")
        else:
            new_balance = round(balance - wit, 2)
            print(f'{wit:.2f}', "withdrawn successfully.  Your new balance is: ", f'{new_balance:.2f}')
            looper_2 = False
    return new_balance

# Exit Function
def ex_4():
    print("\nThank you for using AToM ATM!  Goodbye!")
    quit()

# Choice Function
def choice(balance):
    # Establish Local Variable
    new_balance = balance
    looper_3 = True
    while looper_3:
        try:
            choice = int(input("\nPlease ener your choice:  "))
            if choice <= 0 or choice >= 5:
                raise not_allowed
        except ValueError:
            print("There are only four options.  Please enter 1, 2, 3, or 4.")
        except not_allowed:
            print("There are only four options.  Please enter 1, 2, 3, or 4.")
        else:
            looper_3 = False
            if choice == 1:
                check(balance)
            elif choice == 2:
                new_balance = deposit(balance)
            elif choice == 3:
                new_balance = withdrawal(balance)
            elif choice == 4:
                ex_4()
            else:
                pass
    return new_balance


# Start Program
while True:
    display()
    balance = choice(balance)