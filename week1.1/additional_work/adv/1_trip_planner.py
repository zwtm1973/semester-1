"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

try:
    destination = str(input("Where are you going to? "))

    distance_miles_input = float(input("How many miles will you travel? "))
    time_hours_input = float(input("How many hours will the journey take? "))
except:
    print("Invalid type for one of the inputs.")
    exit()

# TODO: convert distance_miles_input and time_hours_input to numbers
# TODO: calculate the average speed in miles per hour
# TODO: print a summary message using an f-string
# Extension: add validation for zero or negative values

if distance_miles_input <= 0 or time_hours_input <= 0:
    print("A value is 0 or negative.")
    exit()

ave_spd = round(distance_miles_input / time_hours_input, 2)
display_spd = str(ave_spd) + " Mph"

print(f"The average speed for this journey should be {display_spd}.")