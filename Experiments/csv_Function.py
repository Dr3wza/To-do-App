import csv

with open("../weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

# row represents the columns in weather.csv
# data represents the rows in weather.csv
for row in data[1:]:
    if row[0] == city:
        print(row[1])
