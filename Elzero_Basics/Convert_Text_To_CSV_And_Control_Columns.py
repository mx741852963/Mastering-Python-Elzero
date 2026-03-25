# Convert Text To CSV
import csv

# with open('new_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

a = open('new_data.csv', 'r')
reader = csv.reader(a)
file = open('new_data.csv', 'w', newline='')
# file = open('new_data.csv', 'a', newline='')
writer = csv.writer(file)
writer.writerows([["One", "Two"], ["Three", "four"], ["five", "six"], ["seven", "eight"]])
# writer.writerow(["One", "Two", "Three", "four", "five", "six", "seven", "eight"])
# writer.writerows(["One", "Two", "Three", "four", "five", "six", "seven", "eight"])
# writer.writerow(['Ahmad'])
# writer.writerow(['Ahmad'])
# writer.writerow(['Ahmad'])
# print(reader.__next__())
# print(reader.__next__())
# print(reader.__next__())
# print(reader.__next__()) # Error
# for row in reader:
# columns = ['Name', 'Points']
# rows = [['Ahmad', 100], ['Samer', 200]]

# with open('new_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(columns)
#     writer.writerows(rows)
