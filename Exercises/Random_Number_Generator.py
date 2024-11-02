import random


lower_limit = int(input("Enter the lower bound: "))
upper_limit = int(input("Enter the upper bound: "))

if upper_limit < lower_limit:
    print("Please enter suitable bounds")

else:
    number = random.randrange(lower_limit, upper_limit + 1, 1)
    print(number)

