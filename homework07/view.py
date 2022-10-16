from fileinput import filename
import model as m

def check_for_num(data: str):
    while not data.isdigit():
        data = input('Введено неверное значение. Повторите ввод\n')
    return data

def show_menu():
    print('Выберите действие\n\
1 - показать весь справочник\n\
2 - найти контакт по фамилии\n\
3 - найти контакт по номеру телефона\n\
4 - добавить контакт вручную\n\
5 - добавить контакт из файла\n\
6 - сохранить справочник в текстовый файл\n\
7 - завершить работу\n')
    choice = int(check_for_num(input()))
    return choice

def show_phonebook():
    data = m.read_phonebook()
    fields = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']
    output = [dict(zip(fields, record)) for record in data]
    for line in output:
        for key, value in line.items():
            print(f'{key}: {value}')
        print('\n')

def get_filename():
    name = input('Введите имя файла\n')
    return name