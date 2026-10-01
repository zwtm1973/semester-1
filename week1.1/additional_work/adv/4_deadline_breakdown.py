"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

try:
    minutes_remaining_input = int(input("Minutes remaining until the deadline: "))
except:
    print("Numbers only, please.")
    exit()

# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead

if minutes_remaining_input <= 0:
    print("Sorry, but the deadline has already passed.")
    exit()

days_left = int(minutes_remaining_input / 1440)
leftover_mins = minutes_remaining_input % 1440
hours_left = int(leftover_mins / 60)
mins_left = leftover_mins & 60

print(f"There are exactly {days_left} days, {hours_left} hours, and {mins_left} minutes left.")