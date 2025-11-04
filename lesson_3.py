# def a (b):
#     c = 0
#     for i in b:
#         c += i
#     return c 
# numbers = [1,2,3,4,5,6,7]
# print("= ", a (numbers))

# def менин_len(тизме):
#     санак = 0
#     for i in тизме:
#         санак += 1
#     return санак

# сандар = [1,2,3,4,5,6]
# узундук = менин_len(сандар)

# print("Тизмедеги элементтер саны =", узундук)

# def kv (num):
#     rezult = num ** 2
#     return rezult
# for i in range(1, 11):
#     print(i, "=", kv(i))


# b = [1,9,3]
# c= 0
# a = 0
# f = 0
# d = 0
# for i in range(1,10):
#     c += 1
#     if b[0] ==  i:
#         a += i
#     elif b[1] == i:
#         f += i
#     elif b[2] == i:
#         d += i
#     else:
#         continue

# print(f"{b} = {list((a,f,d))} = {c}")

# def demons_som(amount):
#     denoms = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
#     result = {}

#     for d in denoms:
#         count = amount // d
#         if count > 0:
#             result[d] = count
#             amount -= d * count

#     return result

# s = int(input("Сом суммасын киргизиңиз : "))

# parts = demons_som(s)

# print("\nАкча бөлүнүшү:")
# for denom, count in parts.items():
#     print(f"{count} x {denom} сом")







# python3 -m venv venv

# venv/Scripts/activate --> windows
# source venv/bin/activate --> mac or linux

# deactivate

# pip install <package-name>

# pip freeze > requirements.txt

# pip install -r requirements.txt
# """

# import math

# print(math.sqrt(4))
# from colorama import Back, Fore, Style

# print(Fore.RED + "some red text")
# print(Back.GREEN + "and with a green background")
# print(Style.RESET_ALL)

# print(Style.DIM + "and in dim text")
# print("back to normal now")
# import qrcode

# img = qrcode.make("Some data here")
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")

# Виртуальные окружения. --> create venv
# Встроенные модули Python. --> 10 module
# Создание собственных модулей. --> 2 def --> use
# Регулярные выражения. --> 4 primer


# from main2 import greate

# print(greate("islam"))
import re

# pattern = r"\d+"
# string = "abc123def"
# match = re.search(pattern, string)

# if match:
#     print("Совпадение найдено:", match.group())
# else:
#     print("Совпадение не найдено")

email = "duishobaevnn islam01@gmail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@gmail.com$"
if re.match(pattern, email):
    print(True)
else:
    print(False)

# 1 Модуль Match
# import math

# # Вычисление квадратного корня
# sqrt_value = math.sqrt()
# print(f"Квадратный корень из 16: {sqrt_value}")

# # Вычисление синуса угла в радианах
# sin_value = math.sin(math.pi / 2)
# print(f"Синус угла 90 градусов: {sin_value}")

# 2 Модуль Datetime
# import datetime

# # Получение текущей даты и времени
# current_datetime = datetime.datetime.now()
# print(f"Текущая дата и время: {current_datetime}")

# # Форматирование даты
# formatted_date = current_datetime.strftime("%Y-%m-%d")
# print(f"Форматированная дата: {formatted_date}")

# 3 Модуль Os
# import os

# Получение текущего рабочего каталога
# current_dir = os.getcwd()
# print(f"Текущий рабочий каталог: {current_dir}")

# Получение списка файлов в директории
# files = os.listdir(current_dir)
# print(f"Файлы в текущем каталоге: {files}")

# 4 Модуль Random
# import random

# random_1 = random.randint(1, 10)
# print(random_1)

# fruits = ["banana", "apple", "kiwi", "orange"]
# fruits1 = random.choice(fruits)
# print(fruits1)









    
