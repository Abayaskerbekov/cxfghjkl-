# # Мини Проект
# while True:
#     print("\n=== Калькулятор ===")
#     print("1 - кошуу (+)")
#     print("2 - кемитуу (-)")
#     print("3 - кобойтуу (*)")
#     print("4 - болуу (/)")
#     print("0 - чыгуу")

#     choice = input("бироону танда (0 - 4): ")

#     if choice == '0':
#         print("жабылды кет бар")
#         break

#     a = float(input("cанды киргиз:"))

#     b = float(input("экинчи санды киргиз: "))

#     if choice == '1':
#         print(f"жооп: {a} + {b} = {a + b}")
#     elif choice == '2':
#         print(f"жооп: {a} - {b} = {a - b}")
#     elif choice == '3':
#         print(f"жооп: {a} * {b} = {a * b}")
#     elif choice == '4':
#         if b != 0:
#             print(f"жооп: {a} / {b} = {a / b}")
#         else:
#             print("нолго болгонго болбойт")
#     else:
#         print("туура эмес тандоо (ERROR)")




# valut = ["euro","dollar","rub"]
# money = [101.2, 87.0, 1.05]

# euro = 101.2
# dollar = 87.0
# rub = 1.05

# valut = input("\033[034mchoose one?(euro,dollar,rub): ")
# summ = float(input("\033[034mHow much money: "))

# if valut == "euro":
#     rezult = summ * euro
#     print(f"\033[033m{summ} euro = {rezult} som")
# elif valut =="dollar":
#     rezult = summ * dollar
#     print(f"\033[035m{summ} dollar = {rezult} som")
# elif valut =="rub":
#     rezult = summ * rub
#     print(f"\033[036{summ} rub = {rezult} som")
# else:
#     print("\033[031merror")

#  \033[31m-red 32-green 33-yellow 34-blue 35-purple 36-cian