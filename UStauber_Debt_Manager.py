# Programmer:  Ursula Stauber
# Program:  Credit Card Debt Manager
# Project 1
# CIS 1220
# Accuracy of the calculation can be checked with https://www.bankrate.com/credit-cards/tools/credit-card-payoff-calculator/

import math

# Create Negative Number Class for User Input Handling
class NegativeNumber(Exception):
    pass

# Create Warning Class for User Input Handling
class Counseling(Exception):
    pass

# Display a welcome message.
print("Welcome to Debt Manager!")
print("Use this program to figure out how long it will take you to pay of your credit card.")

# Input balance.
looper_1 = True
while looper_1:
    try:
        b = float(input("\nWhat is your credit card balance?  "))
        if b < 0.01:
            raise NegativeNumber
    except ValueError:
        print("Please enter a dollar amount.")
    except NegativeNumber:
        print("You cannot have a negative balance.  Please enter a dollar amount.")
    else:
        looper_1 = False

# Input monthly payment.
looper_2 = True
while looper_2:
    try:
        p = float(input("\nHow much do you pay toward your balance each month?  "))
        if p < 0.01:
            raise NegativeNumber
    except ValueError:
        print("Please enter a dollar amount.")
    except NegativeNumber:
        print("You must make a monthly payment to pay off your debt.  Please enter a dollar amount.")
    else:
        looper_2 = False

# Input interest rate.
looper_3 = True
while looper_3:
    try:
        APR = float(input("\nWhat is your APR (enter as a decimal --> 10% = 0.10)?  "))
        if APR <= 0:
            raise NegativeNumber
        if APR >= 0.37:
            raise Counseling
    except ValueError:
        print("Please enter a decimal amount for your APR.")
    except NegativeNumber:
        print("You must have an APR greater than 0.00 to use this program.")
        print("Please enter a decimal amount for your APR.")
    except Counseling:
        print("\nYou have a very high APR.  Many states cap credit card interest rates.")
        print("Credit card interest rates are also capped for active military service members and their dependants.")
        print("We recommend trying to negotiate a lower rate with your card issuer.")
        print("You can also try transferring your balance to a card with a lower rate.")
        print("Finally, you can also seek help from a debt management organization.")
        print("The National Foundation for Credit Card Counseling can help you find services in your area.")
        print("Try this program with a lower APR to see that your debt can be paid off sooner with a lower APR.")
    else:
        i = float(APR / 365)  # Calculate daily interest rate.
        looper_3 = False

# Calculate how long it will take to pay off a credit card debit.
N = - (1/30) * ((math.log (1 +((b/p) *(1 - ((1 + i)**30))))) / (math.log (1 + i)))
rounded_N = round(N)

# Display the result.
print("\nIt will take you " + str(rounded_N) + " months to pay off your credit card.")

# Display goodbye message.
print("\nThank you for using Credit Card Debt Manager!  Goodbye!")