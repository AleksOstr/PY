def check_for_number(data: str):
    while not data.isdigit():
        data = input('Введено неверное значение. Повторите ввод.\n')
    return data

def main_menu():
    print('Выберите необходимое действие:\n\
1. Найти сотрудника\n\
2. Сделать выборку сотрудников по должности\n\
3. Сделать выборку сотрудников по зарплате\n\
4. Добавить сотрудника\n\
5. Удалить сотрудника\n\
6. Обновить данные сотрудника\n\
7. Экспортировать данные в формате json\n\
8. Экспортировать данные в формате csv\n\
9. Завершить работу')
    return int(check_for_number(input()))

def show_employee(employee: dict):
    fields = ['ID','Фамилия','Имя','Должность','Зарплата','Телефон']
    output = dict(zip(fields, list(employee.values())))
    for key, value in output.items():
        print(f'{key}: {value}', end=' ')