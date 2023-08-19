def Phonebook():
    action = -1
    filename = 'phonebook.txt'
    while action != 0:
        print('Выберите одно из действий:')
        print('1 — Вывести справочник')
        print('2 — Добавить данные')
        print('3 — Изменить данные')
        print('4 — Удалить данные')
        print('0 — Выход из программы')
        action = int(input('Действие: '))
        if action == 1:
            read_txt(filename)
        elif action == 2:
            add_user(filename)
        elif action == 3:
            edit_data(filename)
        elif action == 4:
            delete_data(filename)
        else:
            action = 0
    print('До свидания!')

# Показывает информацию в файле
def read_txt(filename):
    print('\nПП , ФИО , Телефон')
    with open(filename, 'r', encoding='utf-8') as data:
        print(data.read())
print()

# Записывает информацию в файл
def add_user(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        phone_book = data.read()
        num = len(phone_book.split('\n'))
    with open(filename, 'a', encoding='utf-8') as data:
        name = input('Введите ФИО: ')
        phone_number = input('Введите номер телефона: ')
        data.write(f'{num} , {name} , {phone_number}\n')
    print(f'Добавлена запись : {num} , {name} , {phone_number}\n')

# Изменяет информацию из файла
def edit_data(filename):
    print('\nПП , ФИО , Телефон')
    with open(filename, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
    print()
    try:
        index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
        tel_book_lines = tel_book.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(',')
        name = input('Введите ФИО: ')
        phone = input('Введите номер телефона: ')
        num = elements[0]
        if len(name) == 0:
            name = elements[1]
        if len(phone) == 0:
            phone = elements[2]
        edited_line = f'{num}, {name} , {phone}'
        tel_book_lines[index_delete_data] = edited_line
        print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(tel_book_lines))
    except IndexError:
        print('Ошибка: Некорректный номер строки')
    except ValueError:
        print('Ошибка: Введите корректное число')

# Удаляет информацию из файла
def delete_data(filename):
    print('\nПП , ФИО , Телефон')
    with open(filename, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
    print()
    try:
        index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f'Удалена запись: {del_tel_book_lines}\n')
        with open(filename, 'w', encoding='utf-8') as data:
            data.write('\n'.join(tel_book_lines))
    except IndexError:
        print('Ошибка: Некорректный номер строки')
    except ValueError:
        print('Ошибка: Введите корректное число')
        
Phonebook()