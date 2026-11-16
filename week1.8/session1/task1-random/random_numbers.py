import random

# Get user to input how many random numbers they want
amount = int(input("How many numbers? "))

# Generate this many random numbers
randoms = []
random_string = ""
for i in range(amount):
    r = random.randint(0, 10000)
    randoms.append(r)
    random_string += str(r) + "\n"

# Write the random numbers to a file named random.txt, one number per line
random_txt = open("/workspaces/semester-1/week1.8/session1/task1-random/random.txt", "w")

random_txt.write(random_string)