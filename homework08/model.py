import view
import csv
import json

def read_csv(filename: str):
    with open('databse.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
    database = []
    for row in reader:
        employee = {}
        employee['id'] = row[0]
        employee['last_name'] = row[1]
        employee['first_name'] = row[2]
        employee['position'] = row[3]
        employee['salary'] = row[4]
        employee['phone'] = row[5]
        database.append(employee)
    return database