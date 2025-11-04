"""comment
print()

"""

#  ДЗ 1
# summa = float(input())
# summa_2 = int(input())
# if summa < 5000:
#     rate = 9
# elif summa < 10000:
#     rate = 11
# else:
#     rate = 13 
# num = summa * rate / 100 * (summa_2 / 12)
# print(f"{rate}%")
# print(f"job {num:.2f} сом")


# # ДЗ 2
# # photo = int(input())
# # price_per_photo = 10  
# # total = photo * price_per_photo
# # if photo > 10:
# #     total *= 0.95  
# # print(f"сумма {total:.2f} сом")

# # ДЗ 3
# # a = int(input("Биринчи сан: "))
# # b = int(input("Экинчи сан: "))
# # if a < b:
# #     small = a + b
# #     large = a * b
# # else:
# #     small = a * b
# #     large = a + b

# # ДЗ 4 
# # print(f"Кичинеси: {small}, чоңу: {large}")
# # a = int(input("Биринчи баланын жашы: "))
# # b = int(input("Экинчи баланын жашы: "))
# # c = int(input("Үчүнчү баланын жашы: "))
# # max_age = max(a, b, c)
# # print(f"Эң улуу бала {max_age} жашта.")

# #  ДЗ 5
# # a = int(input("a = "))
# # b = int(input("b = "))
# # c = int(input("c = "))

# # nums = [a, b, c]
# # nums.sort()
# # print("Өсүү тартибинде:", nums)

# # ДЗ 6
# # amount = float(input("Сатып алуу: "))

# # if amount > 1000:
# #     amount *= 0.9

# # print(f"төлөм: {amount:.2f} сом")

# # ДЗ 7
# # import math

# # n = int(input("Санды киргизиңиз: "))

# # if n % 2 == 0:
# #     print("Квадрат:", n ** 2)
# # else:
# #     print("Квадрат:", math.sqrt(n))

# #   ДЗ 8
# # my_list = [123, 23, 254, 232]
# # print(max(my_list))

# #  ДЗ 9 
# # a = float(input("биринчи сан"))
# # b = float(input("экинчи сан"))
# # if a > b:
# #     print(f"{a} > {b}")
# # elif a < b:
# #     print(f"{a} < {b}")
# # else:
# #     print(f"{a} = {b}")

# """ if, elif, else/ and or not/><"""
# # sporsmen = (5)
# # su = (0)
# # if sporsmen == 1:
# #     print("sy: ",su +1 )
# # elif sporsmen == 2:
# #     print("su ",su +1,5)
# # else :


# # password1 = input("entr password: ")
# # password2 = input("entr password2: ")

# # if password1 == password2:
# #     print("continue")
# # else:
# #     print("error")
# """str"""


# name = "abdyrazzak"
# print(name.capitalize())# bash tamgany chonoitot
# print(name.encode())# 2 tamgany alyp chygat
# print(name.casefold())# name nin ozun alyp chykty
# print(name.count("a"))# bir tamgany jassan oshol tamgadan kancha bar ekenin sanap beret
# print(name.center)# tushunboi coidum
# print(name.endswith("abdyrazzak")) #karochi tushunbodum
# print(name.expandtabs(2))# tushunbodum
# print(name.find("z"))# tamgany jassan kaisy orunda ekenin aityp beret
# print(name.format())# tushunbodum
# print(name.format_map(""))# tushunbodum
# print(name.index("b"))# index boyuncha kanchanchy turganyn aitat
# print(name.isalnum())# True
# print(name.isalpha())# True
# print(name.isascii())# True
# print(name.isdecimal())# False
# print(name.isdigit())# Flse
# print(name.isidentifier())#True
# print(name.islower())#True
# print(name.isspace())# False
# print(name.isupper())#False
# print(name.istitle())#False
# print(name.join(",,"))# bir tamgany jassan bashyna ayagyna oshol tamgany koyot
# print(name.ljust(1).ljust(2))# tushunbodum
# print(name.lower())# bardygyn kichinekei kylat
# print(name.lstrip("abdy"))# tushundum karochi
# print(name.maketrans)#bilbeim
# print(name.partition("abd"))# ichine emneni jassan oshonu bolup ozuncho chygarat
# print(name.startswith("abdy"))# teksheret parol syaktuu
# print(name.removeprefix("ab"))# karochi name-nin ichindegi tamganyn basynan tamgany jassan oshony ochurot
# print(name.removesuffix("   "))# polnyi name-ni ichindegini jassan baardygyn ochurot
# print(name.replace)# bilbedim
# print(name.rfind("y"))# kanchanchy orunda turganyn tabat
# print(name.rsplit("abdyraz"))
# print(name.rindex("z"))# bir tamgany jassan oshol bar bolso akyrandagyny korgozup beret 
# print(name.rjust(18))# probel koyot
# print(name.rpartition("a"))#akyrkysynan alyp chygat tamgany
# print(name.rstrip("abdyrazzak"))#bardygyn toluk jassan baardygyn ochurot eger toluk jaspasan ochurboit
# print(name.split("a"))# emneni jassan oshonu ochurottuura jassan
# print(name.splitlines())# ech nerse chykpady
# print(name.startswith("abdyrazzak"))# teksheret tuura jaskanyndy True,False
# print(name.strip())# po mestam ochurot
# print(name.swapcase())# baardyk tamgasyn ghonoitot
# print(name.title())#bash tamgasyn chonoitot
# print(name.translate(" "))# tushunbodum
# print(name.upper())#baardygyn chonoitot
# print(name.zfill(10))# tushunbodum




















# import matplotlib.pyplot as plt
# import numpy as np

# # Маалыматтар (жөнөкөй симуляциялык баалар)
# dates = np.arange(1, 15)
# prices = [1.17, 1.168, 1.166, 1.163, 1.162, 1.161, 1.16, 1.158, 1.157, 1.155, 1.153, 1.152, 1.151, 1.15]

# # Колдоо жана каршылык деңгээлдери
# support_levels = [1.155, 1.15]
# resistance_levels = [1.165, 1.17]

# plt.figure(figsize=(10, 6))
# plt.plot(dates, prices, marker='o', label='EUR/USD баа тренди')
# for s in support_levels:
#     plt.axhline(y=s, color='green', linestyle='--', linewidth=1, label=f'Колдоо {s}')
# for r in resistance_levels:
#     plt.axhline(y=r, color='red', linestyle='--', linewidth=1, label=f'Каршылык {r}')

# plt.title('EUR/USD болжолдуу кыймылы (октябрь башы)')
# plt.xlabel('Күндөр')
# plt.ylabel('Баа (EUR/USD)')
# plt.legend(loc='lower right')
# plt.grid(True)
# plt.show()