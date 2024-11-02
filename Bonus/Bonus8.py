date = input("Enter today's date: ")
mood = input ("How do you rate your mood from 1 - 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../Bonus/{date}", "w") as file:
    file.write(mood + "\n")
    file.write(thoughts)