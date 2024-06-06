"""
print(1)

a = 123
b = 1.23
print(a)
print(b)

value = None
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value)

print(type(a)) # функция, которая указывает на тип данных

print(type(b)) # функция, которая указывает на тип данных

s = "hello," # создание 1-ой строки
w = "world" # создание 2-ой строки
print(s, w)


a = 3
b = 11
s = 2022
print(a, b, s)
# print(a,'-'b,'-'s)
print('{} - {} - {}'.format(a,b,s))
print(f'first - {a} second - {b} third - {s}')


print("введите 1-е число: ")
a=input()
print("введите 2-е число: ")
b=input()
print(a, "+",b, "=", a + b)



n = 1.345
print(int(n)) # Отбрасывается дробная часть вне зависимости больше 0.5 или
# меньше
m = "345"
print(m * 2) # При умножении строки на число, она повторяется столько раз на
# какое была умножена
print(int(m) * 2)

n = 1.345
print(str(n) * 2)

n = "1.345"
print(float(n) * 2)
m = 2
print(float(m))

def f(x):
        return x ** 2
print(f(5))

def f(x):
        return x ** 2
g = f

def f(x):
        return x ** 2
g = f
print(f(4)) # 16
print(g(4)) # 16

def calc1(x):
        return x + 10
print(calc1(10)) # 20

def calc2(x):
        return x * 10
def math(op, x):
        print(op(x))
math(calc2, 10) # 100

def calc2(x, y):
        return x + y
def math(op, x, y):
         print(op(x, y))
math(calc2, 10, 45) # 55

def sum(x, y):
        return x + y
def mylt(x, y):
        return x * y

def calc(op, a, b):
        print(op(a, b))
calc(mylt, 4, 5) # 20

def sum(x, y):
        return x + y
f = sum
calc(f, 4, 5) # 9

def sum(x, y):
        return x + y
# ⇔ (равносильно)
sum = lambda x, y: x + y

calc(lambda x, y: x + y, 4, 5) # 9

# Исходный список чисел
numbers = [1, 2, 3, 5, 8, 15, 23, 38]

# Формирование списка пар (число, квадрат числа) для четных чисел
result = [(x, x**2) for x in numbers if x % 2 == 0]

print(result)

# Исходный список чисел
numbers = [1, 2, 3, 5, 8, 15, 23, 38]

# Выбор четных чисел с помощью filter() и lambda
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Создание списка пар (число, квадрат числа) с помощью map() и lambda
result = list(map(lambda x: (x, x**2), even_numbers))

print(result)

list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)

data = '1 2 3 5 8 15 23 38'.split()
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

data = list(map(int,input().split()))

def where(f, col):
        return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res) # [0, 2, 4, 6, 8]

lambda x: x % 2 == 0

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14),
('user5', 7)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]


colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()


with open('file.txt', 'w') as data:
        data.write('line 1\n')
        data.write('line 2\n')


path = 'file.txt'
data = open(path, 'r')
for line in data:
        print(line)
data.close()


colors = ['red', 'green', 'blue']
data = open('file1.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()

colors = ['red', 'green', 'blue']
with open('file2.txt', 'a') as data:
    for color in colors:
        data.write(color + "n")  # Добавляем разделитель в виде перевода строки


# Режим 'w+'
with open('file3.txt', 'w+') as data:
    data.write('line 1/n')
    data.write('line 2/n')
    data.seek(0)  # Перемещаем курсор в начало файла для чтения
    print(data.read())

# Режим 'r+'
with open('file2.txt', 'r+') as data:
    print(data.read())  # Сначала читаем содержимое
    data.write('line 3n')  # Затем дописываем новую строку в конец файла






data = open('phonebook.txt', 'a') 



def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            phout.write(','.join(record.values()) + 'n')

def find_by_lastname(phone_book, lastname):
    return [record for record in phone_book if record['Фамилия'] == lastname]

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)

def show_menu():
    print("nВыберите необходимое действие:n"
          "1. Отобразить весь справочникn"
          "2. Найти абонента по фамилииn"
          "3. Изменить номер телефонаn"
          "4. Удалить абонентаn"
          "5. Добавить абонентаn"
          "6. Сохранить справочникn"
          "7. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            for record in phone_book:
                print(record)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 5:
            user_data = input('Введите данные нового абонента (Фамилия,Имя,Телефон,Описание): ')
            add_user(phone_book, user_data)
        elif choice == 6:
            write_txt('phonebook.txt', phone_book)
            print('Справочник сохранен.')
        else:
            print('Неверный пункт меню.')

        choice = show_menu()

work_with_phonebook()

"""
"""

data = open('phonebook.txt', 'a') 

def change_number(phone_book, lastname, new_number):
    for record in phone_book:
        if record['Фамилия'] == lastname:
            record['Телефон'] = new_number
            return f"Номер телефона абонента {lastname} изменен на {new_number}."
    return "Абонент с такой фамилией не найден."

def delete_by_lastname(phone_book, lastname):
    global phone_book_global
    phone_book_global = [record for record in phone_book if record['Фамилия'] != lastname]
    return f"Абонент с фамилией {lastname} удален из справочника."

def read_txt(filename):
    phone_book = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:  # Предполагается, что есть четыре части на запись
                    phone_book.append({
                        'Фамилия': parts[0].strip(),
                        'Имя': parts[1].strip(),
                        'Телефон': parts[2].strip(),
                        'Описание': parts[3].strip()
                    })
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    return phone_book


def work_with_phonebook():
    phone_book = read_txt('phonebook.txt')

    while True:
        choice = show_menu()

        if choice == 1:
            for record in phone_book:
                print(record)
        elif choice == 2:
            lastname = input('Введите фамилию для поиска: ')
            found = find_by_lastname(phone_book, lastname)
            if found:
                for person in found:
                    print(person)
            else:
                print("Абонент не найден.")
        elif choice == 3:
            lastname = input('Введите фамилию для изменения номера: ')
            new_number = input('Введите новый номер телефона: ')
            print(change_number(phone_book, lastname, new_number))
        elif choice == 4:
            lastname = input('Введите фамилию для удаления абонента: ')
            print(delete_by_lastname(phone_book, lastname))
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

# Остальные функции остаются без изменений

# Глобальная переменная для хранения справочника
phone_book_global = []

# Точка входа в программу
if __name__ == '__main__':
    work_with_phonebook()

"""





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