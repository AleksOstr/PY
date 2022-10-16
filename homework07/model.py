import sys
import view as v


def stop_phonebook():
    sys.exit()

def read_phonebook():
    with open('phonebook.csv', 'r') as file:
        data = [line.strip().split(';') for line in file]
    return data

def add_contact():
    surname = input('Введите фамилию\n')
    name = input('Введите имя\n')
    phone_number = input('Введите телефон\n')
    description = input('Введите описание\n')
    with open('phonebook.csv', 'a') as file:
        file.write('{}; {}; {}; {}\n'.format(surname, name, phone_number, description))
    v.show_menu()

def add_contact_by_txt(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        data = [line.split() for line in file]
    with open('phonebook.csv', 'a') as file:
        for record in data:
            for value in record:
                file.write(f'{value};')
            file.write('\n')
    v.show_menu()

def add_contact_by_csv(filename: str):
    data = []
    with open(filename, 'r') as file:
        data = [line.strip('\n').split(';') for line in file]
    print(data)
    with open('phonebook.csv', 'a') as file:
        for record in data:
            for value in record:
                file.write(f'{value};')
            file.write('\n')
    v.show_menu()

add_contact_by_csv('dotcomma.csv')
