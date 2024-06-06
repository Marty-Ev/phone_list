


def show_menu():
    print("\nВыберите действие:")
    print("1. Показать все контакты")
    print("2. Найти контакт по фамилии")
    print("3. Изменить номер телефона")
    print("4. Удалить контакт")
    print("5. Добавить новый контакт")
    print("6. Сохранить изменения в файл")
    print("7. Выйти из программы")
    try:
        choice = int(input("Ваш выбор: "))
        return choice
    except ValueError:
        print("Пожалуйста, введите число, соответствующее пункту меню.")
        return None

def read_txt(filename):
    phone_book = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    phone_book.append({
                        'Фамилия': parts[0].strip(),
                        'Имя': parts[1].strip(),
                        'Телефон': parts[2].strip(),
                        'Описание': parts[3].strip()
                    })
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as file:
        for record in phone_book:
            file.write(','.join([record['Фамилия'], record['Имя'], record['Телефон'], record['Описание']]) + '\n')

def change_number(phone_book, lastname, new_number):
    for record in phone_book:
        if record['Фамилия'] == lastname:
            record['Телефон'] = new_number
            return f"Номер телефона абонента {lastname} изменен на {new_number}."
    return "Абонент с такой фамилией не найден."

def delete_by_lastname(phone_book, lastname):
    return [record for record in phone_book if record['Фамилия'] != lastname]

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

def work_with_phonebook():
    phone_book = read_txt('phonebook.txt')

    while True:
        choice = show_menu()

        if choice == 1:
            for record in phone_book:
                print(record)
        elif choice == 2:
            lastname = input('Введите фамилию для поиска: ')
            found = [record for record in phone_book if record['Фамилия'] == lastname]
            if found:
                for record in found:
                    print(record)
            else:
                print("Абонент не найден.")
        elif choice == 3:
            lastname = input('Введите фамилию для изменения номера: ')
            new_number = input('Введите новый номер телефона: ')
            print(change_number(phone_book, lastname, new_number))
        elif choice == 4:
            lastname = input('Введите фамилию для удаления абонента: ')
            phone_book = delete_by_lastname(phone_book, lastname)
            print(f"Абонент с фамилией {lastname} удален из справочника.")
        elif choice == 5:
            user_data = input('Введите данные нового абонента (Фамилия,Имя,Телефон,Описание): ')
            add_user(phone_book, user_data)
        elif choice == 6:
            write_txt('phonebook.txt', phone_book)
            print('Справочник сохранен.')
        elif choice == 7:
            print('Работа с телефонным справочником завершена.')
            break
        else:
            print('Неверный пункт меню.')

if __name__ == '__main__':
    work_with_phonebook()
