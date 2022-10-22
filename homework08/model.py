from random import randint
import view
import csv
import json

def read_csv():
    database = []
    with open('database.csv', 'r', encoding='utf-8-sig', newline='\r\n') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            employee = {}
            employee['id'] = int(row[0])
            employee['last_name'] = row[1]
            employee['first_name'] = row[2]
            employee['position'] = row[3]
            employee['salary'] = float(row[4])
            employee['phone'] = row[5]
            database.append(employee)
    return database

def check_id(id: int):
    database = read_csv()
    for employee in database:
        while id == employee['id']:
            id = randint(1, 1000)
    return id

def add_employee():
    employee_info = view.get_employee_info()
    with open('database.csv', 'a', encoding='utf-8', newline='\r\n') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writer.writerow(employee_info.values())
