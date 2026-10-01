"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = float(input("Travel cost in pounds: "))
food_cost_input = float(input("Food cost in pounds: "))
accommodation_cost_input = float(input("Accommodation cost in pounds: "))

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places

total_cost = travel_cost_input + food_cost_input + accommodation_cost_input
ave_cost = total_cost / 3

total_cost = round(total_cost, 2)
ave_cost = round(ave_cost, 2)

print(f"Total cost: £{total_cost}, Average cost: £{ave_cost}")