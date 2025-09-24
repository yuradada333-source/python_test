# Числа(float,int)
# Строки(str)
# import random
# from fileinput import filename
# from itertools import count

# Списки(list) - это изменяемые последовательности элементов.
# Кортежи(tuple) - это неизменяемые последовательности элементо.
# Множества(set) - это неупорядочная последовательность уникальных элементо.

# Славори(dict) - это неупорядочная последовательность элементо.

# import re
# from random import sample
# from xml.sax.handler import property_interning_dict

# Сентябрь
# ______________________________________
# 03.09.2025
# ______________________________________
# Множества

# Пример
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)

# Пример
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)


#  Пример
# users = set
# users_1 = {}
# print(users)
# print(users_1)


#  Пример
# users = {"Tom", "Bob", "Alice", "Tom", "Tom"}
# print(len(users))

#Добавление элементов
#________________________
# rukzak = set()
#
# rukzak.add('Спички')
# rukzak.add('Соль')
# rukzak.add('Топор')
# rukzak.add('Вода')
# rukzak.add(1 + 2)
# print(rukzak)


#Удаление элементов
#_________________________
# users = {"Tom", "Bob", "Alice", "Tom"}
# user = "Tom"
# if user in users:
#     users.remove(user)
# print(users)

# или так
# users = {"Tom", "Bob", "Alice", "Tom"}
# users.remove("Tom")
# print(users)
# ___________________________
#Удаление часть  элементов
#  Пример
# users = {"Tom", "Bob", "Alice", "Tom"}
# users.discard("Tim")
# print(users)
#
# users.discard("Tom")
# print(users)
# ____________________________
#Удаление всех элементов
# users = {"Tom", "Bob", "Alice", "Tom"}
# users.clear()
# print(users)

# __________________________
# Перебор множеств
# users = {"Tom", "Bob", "Alice", "Tom"}
# for user in users:
#     print(user + " Привет!")

# __________________________
# Операции с множествами
# users = {"Tom", "Bob", "Alice", "Tom"}
# students = users.copy()
# print(students == users)

# __________________________
# Операции с множествами
# users = {"Tom", "Bob", "Alice", "Tom"}
# users2 = {"Sam", "Kate", "Bob", "Tom"}
# users3 = users.union(users2)
# print(users3)

# users = {"Tom", "Bob", "Alice", "Tom"}
# users2 = {"Sam", "Kate", "Bob", "Tom"}
# print(users | users2)

# __________________________
# Пересечение множеств
# users = {"Tom", "Bob", "Alice", "Tom"}
# users2 = {"Sam", "Kate", "Bob", "Tom"}
# users3 = users.intersection(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice", "Tom"}
# users2 = {"Sam", "Kate", "Bob", "Tom"}
# print(users & users2)


# __________________________
# Разность множеств
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users3 = users.difference(users2)
# print(users3)

#  Пример symmetric_difference
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users3 = users.symmetric_difference(users2)
# print(users3)
#
# users4 = users ^ users2
# print(users4)

# ________________________________________
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users3 = users.symmetric_difference_update(users2)
# print(users)


# Функция frozen set
# users = frozenset({"Tom", "Bob", "Alice"})
# print(users)


# len(s): возвращает длину множества
# x in s: возвращает True, если элемент x присутствует в множестве s
# x not in s: возвращает True, если элемент x отсутствует в множестве s

# Задача 1
# castle = [1, ['c'], 543, 'P', ['n',['r']], 'i', [[['s']]]]

# print(castle[3] + castle[4][1][0] + castle[5] +castle[4][0] + castle[1][0] + chr(101) + castle[6][0][0][0] + castle[6][0][0][0])
# print(*castle[4][1])
# print(castle[5])
# print(castle[4][0])
# print(*castle[1])
# print(chr(101))
# print(*castle[6][0][0])
# print(*castle[6][0][0])

# Задача 2
# message = [('We',),'rec',{'r':'o'},{'o':'r'},{'m1':'ded'},{'m3':['a'], 'm4':{'m5': 'UFO'}}]
# print(message [0] + message[0][1])



# ______________________________________
#  07.09.2025
# ______________________________________
# Кортежи - это упорядочнная неизменяемая коллекция элементов, которые могут быть разных типов.
# Проще говоря, это как список, но который нельзя изменить после создания.

# Основные кортежи:
#  Упорядочность - элементы хранятся в определенном порядке.
#  Неизменяемость
#  Индексируемость
#  Допускают дубликаты
#  Могут содержать разные типы данных


# Создание кортежей
# emply_tuple = ()
# Кортеж с одним элементом
# single_item = (42,)
# print(type(single_item))


# numbers = (1, 2, 3, 4, 5)

# Кортеж с разными типами данных
# mixed = (1, 'hello', True, 3.14)

# Вложенные кортежи
#
# nested = ((1,2), ('a', 'b'), (True, False))
# print(numbers)
# print(mixed)
# print(nested)


# coordinaters = 10.5, 20.7, 30.9
# print(type(coordinaters))
# x, y, z = coodinaters
# print(x, y, z)

# Преобразование строки в кортеж
# string_to_tuple = tuple('Python')
# print(string_to_tuple)

# Множества в кортеж
# set_to_tuple = tuple({1,2,3})
# print(set_to_tuple)

# Первые три элемента
# first_three = fruits[:3]
# print(first_three)

# От второго до четвертого
# middle = fruits[1:4]
# print(middle)

# Разворот кортежа
# reversed_tuple = fruits[::-1]
# print(reversed_tuple)


# Методы кортежа
# banana_count = fruits.count('banana')
# banana_index = fruits.index('banana')
# print(banana_count)
# print(banana_index)


# fruits = ('apple', 'banana', 'cherry')
# print(len(fruits))
# print(cherry in fruits)


# coordinaters = (10.5, 20.7, 30.7)
# new_coordinaters =(15.0) + coordinaters[1:]
# print(new_coordinaters)

# tuple_with_list = (1, 2, [3,4])
# tuple_with_list[2][0] = 30
# print(tuple_with_list)


# Возврат значений из функции
# def get_user_info():
#     name= 'Anna'
#     age  = 30
#     is_admin = True
#     return  name, age, is_admin
# user_name, user_age, user_is_admin = get_user_info()
# print(f'Name: {user_name}, Age: {user_age}, Admin: {user_is_admin}')

# Фиксированные данные
# days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday')
# today_index = 3
# print(f'Today is {days_of_week[today_index ]}')


# Новая тема
# РАБОТА С ФАЙЛАМИ

# file = open('sample-2.txt', "w")
# print(file.read())
# file.close()

# file = open('sample.txt', "a")
# file.write("\npython")
# file.write("\nhdkufahlkjh")
# file.close()

# file = open('sample-2.txt', "r")
# print(file.read())
# file.close()


# Пример
# Функция with
# with open("sample.txt") as file:
#     print(file.read())

# Функция read
# file.read(size)
#
# file = объект файла
# size = количество символов, которое нужно прочитать. если не указать, то файл прочитаетсяцеликом.

# f = open('sample.txt', 'r')
# print(f.read(7))
# print(f.read(9))



# _____________________________________
# 10.09.2025
# _____________________________________
# Функция reedlines

# x = open("examplr.txt",'r')
# print(x.readline())
# print(x.readlines(2))
# print(x.readlines())

# Функция write
# f = open('examplr2.txt', 'w')
# f.write('Hello \n World')
# f.write('Hello \n World')
# f.write('Hello \n World')
# f.close()


# Функция tell
# with open ('examplr2.txt', 'r') as f:
#     position_before = f.tell()
#     print(f'Позиция до чтения: {position_before}')
#     data = f.read(5)
#     print(f'прочитанные данные: {data}')
#     position_after = f.tell()
#     print(f'Позиция после чтения: {position_after}')


# Функция truncate
# with open ('examplr3.txt', 'w+') as f:
#     f.write('Это очень длиный текст, который мы хотим обрезать.\n')
#     f.seek(0)
#     f.truncate(10)
#     f.seek(0)
#     print(f.read())


# filename = 'test.txt'


# Пример #1
# with open(filename, encoding="utf-8") as file:
#     data = file.read()
#     print(data)

# Пример #2
# with open(filename, encoding="utf-8") as file:
#     data = file.readlines()
#     print(data)

# Пример #3
# with open(filename, encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# import os
# Переименования файла
# os.rename('test.txt', 'test_2.txt')


# Задача 1
# x = open("example3.txt",'r')
# print(x.readline())

# os.rename('example3.txt', 'example4.txt')
# x = open("example4.txt",'r')
# print(x.readline())


# Работа с файлами
# os.system('test_2.txt') создание текст документа
# os.system('Меню игры.png')

# os.system('mkdir test') создание папки


# os.system('python qwerty.py')


# with open('1.txt') as file:
#     str1 = file.read()
#     print(str1)



# with open('1.txt') as file:
#     str1 = file.read()
# word_list = str1.split()
# print(word_list)



# with open('1.txt') as file:
#     str1 = file.read()
# word_list = str1.split()
# result = ''
# for word in word_list:
#     result += word+ ','
# print(result)


# with open('1.txt') as file:
#     str1 = file.read()
# word_list = str1.split()
# result = ','.join(word_list)
# print(result)


# import json
# filename = 'file.json'
# info = {"ФИО": "Иванов И.И",
#         "Оценки": {
#             "Матаматика": 4,
#             "Физика": 5,
#             "Информатика": 5
#         },
#         "Хобби": ["Программирование", "Плавание"],
#         "Возраст": 14,
#         "ДомЖивотные": None
#         }
# with open (filename, "w", encoding="utf-8") as file:
#     file.write(json.dumps(info, ensure_ascii=False, indent=4))
#
#
# info_2 = []
# with open (filename, encoding="utf-8") as file:
#     info_2 = json.loads(file.read())
# print(info_2)


# _____________________________________
# 14.09.2025
# _____________________________________

import requests

# url = 'https://api.chucknorris.io/jokes/random'
# responce = requests.get(url)
# data = responce.json()
# print(data["id"])


# url = 'http://api.weatherapi.com/v1/current.json?key={5a3a99294cd7b724afb8d23e61d488fe}&q={Москва}'
# responce = requests.get(url)
# print(responce)


# Ваш API ключ с сайта OpenWeatherMap
# API_KEY = "5a3a99294cd7b724afb8d23e61d488fe"
# # Город для запроса погоды
# CITY = "Moscow"
# # Формируем URL запроса
# url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
#
# # Отправляем запрос к API
# response = requests.get(url)
# data = response.json()
# print(data['weather'][0]['description'])


# Пример
# # Ваш API ключ с сайта OpenWeatherMap
# API_KEY = "ваш_ключ_сюда"
# # Город для запроса погоды
# CITY = "Moscow"
#
# # Формируем URL запроса
# url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru"
#
# # Отправляем запрос к API
# response = requests.get(url)
# data = response.json()
#
# # Проверяем успешность запроса
# if data["cod"] == 200:
#     # Извлекаем данные о погоде
#     weather = data["weather"][0]["description"]
#     temp = data["main"]["temp"]
#     feels_like = data["main"]["feels_like"]
#     humidity = data["main"]["humidity"]
#
#     # Выводим результат
#     print(f"Погода в {CITY}:")
#     print(f"Температура: {temp}°C (ощущается как {feels_like}°C)")
#     print(f"Описание: {weather.capitalize()}")
#     print(f"Влажность: {humidity}%")
# else:
#     print("Ошибка получения данных о погоде")


# Пример 2
# url = f"http://randomuser.me/api"
# #
# responce = requests.get(url)
# data = responce.json()
# print(data)
# print(f"Name: {data['results'][0]['name']['first']}")


# Работа с CSV
# import csv
#
# filename = "test.csv"
#
# shop_list = {"картофель": [2, 100], "яблоки": [3, 250], "морковь": [1, 35]}
#
# # Запись в файл
# with open(filename, "w", encoding="utf-8", newline="") as file:
#    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
#    writer.writerow(["Наименование", "Вес", "Цена/кг."])  # Заголовки столбца
#
#    for name, values in sorted(shop_list.items()):
#        writer.writerow([name, *values])
#    writer.writerow(["мука", "4", "70"])  # Допишем произвольную запись
# # Чтение файла
# rows = []
# with open(filename, "r", encoding="utf-8") as file:
#    reader = csv.reader(file)
#    rows = list(reader)  # reader - итерируемый объект и может быть преобразован в список строк
#
# for row in rows:
#    print(row)




# Задача 1
# import pprint
# import json
# filename = 'file.json'
# info = {"ФИО": "Юртаев Ю.А",
#         "Д/с": {
#             "Аленка": "АПС_аналоговое",
#             "Сказка": "АПС_аналоговое",
#             "Золотая рыбка": "АПС_адресная"
#         },
#         "Район": ["новый город"],
#         "Выезд": "авто",
#         "Неисправность": None
#         }
# with open (filename, "w", encoding="utf-8") as file:
#     file.write(json.dumps(info, ensure_ascii=False, indent=4))
#
#
# info_2 = []
# with open (filename, encoding="utf-8") as file:
#     info_2 = json.loads(file.read())
# print(info_2)

# _________________________
# 17.09.20
# _________________________
# Новая тема Git
# ___________________________

# _____________________________
# 24.09.2025
# _____________________________


















