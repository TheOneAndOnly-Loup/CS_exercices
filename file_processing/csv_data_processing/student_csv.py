import csv

fields = ['StudentID', 'Name', 'Major']
rows = [
    ['1', 'Alice', 'Computer Science'],
    ['2', 'Bob', 'Mathematics'],
    ['3', 'Charlie', 'Physics'],
    ['4', 'David', 'Biology'],
    ['5', 'Eve', 'Chemistry'],
    ['6', 'Frank', 'Computer Science'],
    ['7', 'Grace', 'Computer Science']
]

filename = 'students.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open(filename, "r") as csvfile:
    content = csv.DictReader(csvfile)
    for row in content:
        print(row)