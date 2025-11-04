# text = "hfiufhiuerhhdsfhiuwereewabbascsbgcccbhdbhbabavsgcbcbxhsha"
# a = ""
# b = ""
# c = ""
# for i in text:
#     if i == 'a' or i == 'b' or i == 'c':
#         print(i)
#     else:
#         continue

# enter_num = input("enter number:")
# for i in range(1, 10, ):
#     p = int(enter_num) * i
#     print(f"{enter_num}*{i}={p}")
# for i in range(1, 100):
#     if i == 50:
#         break
#     elif i == 10:
#         continue
#     else:
#         print(i)


# dollar = "purchase"-87.0,"sale"-87.5,
# euro = "purchase"-100.8,"sale"-101.8,
# rub = "purchase"-1.06,"sale"-1.09,
# kaz = "purchase"-0.150,"sale"-0.168,


# 1 DOM ZADANIA

# a = int(input())
# b = int(input())
# c = int(input())

# if min(a, b, c,)**2 > max(a, b, c,):
#     print(min(a, b, c,))
# if max(a, b, c,)**2 > min(a, b, c):
#     print(max(a, b, c,))
# else:
#     print(max(a, b, c,))
# float_number = 24

# entrance_number = (float_number - 1) // 20 + 1
# floor_number = (float_number - 1) % 20 // 4 + 1
# print(entrance_number)
# print(floor_number)

# x = 10
# y = 9
# is_equal = x != y



# 2 DOM ZADANIA

# for i in range(1, 10):
#     for j in range(1,10):
#         print(f"{i}*{j}={i*j}")

# enter_num = input("enter number:")
# for i in range(1, 10):
#     p = int(enter_num)* i
#     print(f"{enter_num}*{i}={p}")

# 3 DOM ZAADANIA
# name = "abdyrazzak"
# print(name.capitalize())
# print(name.encode())
# print(name.casefold())
# print(name.count("a"))
# print(name.center)
# print(name.endswith("abdyrazzak")) 
# print(name.expandtabs(2))
# print(name.find("z"))
# print(name.index("b"))
# print(name.rfind("y"))
# print(name.rsplit("abdyraz"))
# print(name.rindex("z"))
# print(name.rjust(18))
# print(name.rpartition("a"))
# print(name.rstrip("abdyrazzak"))
# print(name.split("a"))
# print(name.splitlines())
# print(name.startswith("abdyrazzak"))
# print(name.strip())
# print(name.swapcase())
# print(name.title())


# n = 0
# while n <= 9:
#     n += 1
#     if n % 2 == 1:
#         print(n, " i love you ")
#     elif n == 4:
#         continue
#     elif n == 8:
#         break
#     else:
#         print(n, " i dontlove you ")


  
# password = "12345"
# enter = input("enter: ")
# c = 0
# while password != enter:
#     c += 1
#     if c == 10:
#         print(" you are blocked")
#         break
#     else:
#         enter = input("erroe enter again: ")
# else:
#     print("success", c)







# email = "admin@gmail.com"
# password = "admin111"
# count = 0

# while True:
#         enter_email = input("enter email: ")
#         enter_password = input("enter password: ")
#         count += 1

#         if "@gmail.com" not in enter_email:
#             # if "@gmail.com" not in enter_email:
#             print("Email должен заканчиваться на '@gmail.com'")    
#             continue
#         if enter_email[0] == '_' or enter_email[-1] == ".":
#               print("Email должен заканчиваться на '.'")
#               continue
#         if len(enter_password) < 8:
#               print("password > 8 !!! ")
#               continue
#         if count == 8:
#               print("you are blocked")
#               break
#         else:
#               if enter_email == email and enter_password == password:
#                     print("Вход выполнен успешно")
#                     break
#               else:
#                     print("Неправилный email или паролью")
                    

# sport = ["football", "volleyball", "ufc"]
# sport.append("basketball")
# print(sport)
# sport.pop(0)
# print(sport)
# sport[2] = "boks"
# print(sport)
# sport.remove("ufc")
# print(sport)
# sport.append("tennis")
# print(sport)
# my_numbers = [12,3,32,54,2,3,1,10,12]
# print(max(my_numbers))
# print(min(my_numbers))
# print(sum(my_numbers))
# print(len(my_numbers))
# print(sorted(my_numbers))
# my_numbers.sort()
# print(my_numbers)

# valut = ('rub', 'dollar', 'euro' )
# sum_valut = [1.12, 87, 102 ]

# if valut == sum_valut:
#     sum_valut (0) == valut(0)
#     print(input(0))
# elif valut == sum_valut:
#     sum_valut (1) == valut(1)
#     print(input(1))
# elif valut == sum_valut:
#     sum_valut (2) == valut(2)
#     print(input(2))
# else:
#     print("error")

# def p (a, b):
#     n = (a * b)
#     return n 
# print(p(5, 6))                                                                                                                      

# def hello():
#     print("hello")
# hello() 
          
# def plus (a, b, c, d):
#     return (a + b ) * c / d
# print(plus(2, 4, 5, 2))
          
# def name(text):
#     for i in list(text):
#         print(i.upper)
# name("islam")
                                  