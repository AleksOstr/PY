from random import randint
import view
import csv
import json
import sys
import controller


def stop_programm():
    sys.exit()

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

def find_employee(last_name):
    database = read_csv()
    for employee in database:
        if last_name.lower() in employee['last_name'].lower():
            view.show_employee(employee)

def job_selection(job):
    database = read_csv()
    for employee in database:
        if job.lower() in employee['position'].lower():
            view.show_employee(employee)

def sample_by_salary(salary_range: list):
    database = read_csv()
    for employee in database:
        if min(salary_range) <= employee['salary'] <= max(salary_range):
            view.show_employee(employee)

def delete_employee(id: int):
    database = read_csv()
    for employee in database:
        if id == employee['id']:
            database.pop(database.index(employee))
    with open('database.csv', 'w', encoding='utf-8', newline='\r\n') as f:
        csv_writer = csv.writer(f, delimiter=';')
        for employee in database:
            csv_writer.writerow(employee.values())

def update_employee(id: int):
    database = read_csv()
    for employee in database:
        if id == employee['id']:
            employee = view.get_updated_info(employee)
    with open('database.csv', 'w', encoding='utf-8', newline='\r\n') as f:
        csv_writer = csv.writer(f, delimiter=';')
        for employee in database:
            csv_writer.writerow(employee.values())

def export_json():
    database = read_csv()
    with open('database.json', 'w') as f:
        json.dump(database, f)