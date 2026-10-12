# Worksheet 1.2: Task 1 Solution
import sys

try:
    result = int(input("Enter an integer grade between 0 and 100: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if not (0 <= result <= 100):
    sys.exit("Error: Grade must be an integer between 0 and 100")

if result >= 70:
    grade =  "distinction"
elif result >= 40:
    grade = "pass"
else:
    grade = "fail"

print(f"{result} is a {grade}")