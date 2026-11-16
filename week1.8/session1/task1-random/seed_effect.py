# See README.md for instructions on what to do this program

import random

random.seed(11)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

#If there is no seed given, the functions use the system time as the seed. if the same seed is used the same 'random' sequence is recieved.