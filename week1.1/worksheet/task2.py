"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jack Whitworth
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

try:
    save_amount = int(input("How much money would you like to save every month? (Integers only): "))
except:
    print("Invalid amount")
    exit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

total_saved = save_amount * 12
print(f"You will have saved {total_saved} pounds in a year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest_total = total_saved + (total_saved * 0.008)

print(f"Including interest, this total would be £{interest_total:.2f}.")