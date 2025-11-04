# file = open("book.txt","w")
# print(*file)
# print(file.readline())
# print(file.readline())
# print(file.tell)
# print(file.seek())
# file.close()



# def read_book():
#     file = open("book1.txt","w")
#     print(file.write("abdu2\naskarov\n17"))
#     print(file.writelines("full_code"))
#     file.close()


# read_book()


# def w ():
#     file = open("book2.txt","x")
#     print(file.write("abdu"))
    
# w()
# def a ():
#     file = open("book1.txt","r")
#     print(file)
#     file.close()

# a()



# import random

# st = ["abdu", "nurbol", "elhan", "baitoro", "kylych"]

# def students(arr):
#     with open("st.txt","a") as file:
#         for i in arr:
#             file.write(i + "\n")
# students(st)


# qua = ["print", "input", "for while", "def", ]

# def fullcode(ans):
#     with open("qua.txt","a") as file:
#         for i in ans:
#             file.write(i + "\n")
# fullcode(qua)

# def read_st():
#     with open ("st.txt") as file:
#         return random.choice(file.readlines())

# print(read_st)

# def read_qua():
#     with open ("qua.txt") as file:
#         return random.choice(file.readlines())
    
# print(read_qua)


# Мини Проект
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



# 1 DZ
# nums = [23,34,5,6,7,43,76,3,57]
# for i in range (len(nums)):
#     for j in range (len(nums)-1):
#         if nums[j]>nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

# nums = [21,23,43,1,1,23,22]
# nums.sort()
# print(nums)

# def num(num2,num3):
#     low = 0
#     num4 = False

#     while low < len(num2) and not num4:
#         if num2[low] == num3:
#             num4 = True
#         else:
#             low += 1
#     return num4

# num5 = [23,3,43,3,54,4,65,7,4,23]
# value = 33
# rezult = num(num5, value)
# if rezult:
#     print("tabyldy")
# else:
#     print("error")


# def num1(num2, num3):
#     low = 0
#     high = len(num2) - 1
#     num4 = False

#     while low <= high and not num4:
#         middle = (low + high) // 2
#         guess = num2[middle]
#         if guess == num3:
#             num4 = True
#             return num4
#         if guess > num3:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return num4

# num2 = [1,2,3,4,5,11,12,13,25,28,33,45,89,93]
# value = 157
# rezult = num1(num2, value)

# if rezult:
#     print("tuura")
# else:
#     print("error")
            


# 3 DZ
# def num (n):
#     if n == 1:
#         return 1
#     return n * num(n - 1)
# print(num(6))



# n = {
#     "name" : "abdy",
#     "year" : 18,
#     "from" : "Kyrgyzstan",
#     "city" : "bishkek",
#     "real city" : "manas"
# }

# print(n["from"])
# print(n["name"])




