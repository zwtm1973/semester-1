# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()

minimum = min(numbers)
maximum = max(numbers)

mean = sum(numbers)/len(numbers)

if len(numbers) % 2 != 0:
    index = int((len(numbers)-1)/2)
    median = numbers[index]
else:
    index = int((len(numbers))/2)
    num1 = numbers[index]
    num2 = numbers[index - 1]
    median = sum([num1, num2])/2

print(f"Minimum = {minimum}\nMaximum = {maximum}\nMean = {mean}\nMedian = {median}")
