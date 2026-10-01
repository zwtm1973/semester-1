"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

try:
    numerator_input = int(input("Enter the numerator: "))
    denominator_input = int(input("Enter the denominator: "))
except:
    print("Only numbers can be inputted.")
    exit()

# TODO: wrap the risky operations in a try/except block
# TODO: convert the values to integers and perform the division
# TODO: print clear feedback when something goes wrong
# TODO: only show the answer when the division succeeds

if denominator_input == 0:
    print("Cannot divide by zero.")
    exit()

division_result = numerator_input / denominator_input

print(f"This is the division result: {division_result}.")