import sys
import view as v


def stop_phonebook():
    sys.exit()

def read_phonebook():
    with open('phonebook.csv', 'r') as file:
        data = [line.strip().split(';') for line in file]
    fields = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']
    output = [dict(zip(fields, record)) for record in data]
    return output

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
    with open('phonebook.csv', 'a') as file:
        for record in data:
            for value in record:
                file.write(f'{value};')
            file.write('\n')
    v.show_menu()

def export_to_txt():
    records = read_phonebook()
    with open('phonebook.txt', 'a') as file:
        for record in records:
            file.write(' '.join(record))
            file.write('\n')
    v.show_menu()

def find_by_phonenumber():
    data = read_phonebook()
    phone_number = input('Укажите номер телефона\n')
    flag = False
    for i in range(len(data)):
        for key, value in data[i].items():
            if phone_number in value:
                flag = True
                v.show_contact(i)
    if not flag:
        print('Номер не найден\n')
    v.show_menu()
            
def find_by_surname():
    data = read_phonebook()
    surname = input('Введите фамилию\n')
    flag = False
    for i in range(len(data)):
        for key, value in data[i].items():
            if surname.lower() in value.lower():
                flag = True
                v.show_contact(i)
    if not flag:
        print('Совпадений не найдено')
    v.show_menu()