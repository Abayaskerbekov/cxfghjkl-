"""
Введение в ООП.     
"""

# # Класс аныктайбыз
# class Car:
#     # Куруучу метод (конструктор)
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     # Метод
#     def drive(self):
#         print(f"{self.brand} унаасы жүрүп жатат!")

# # Объекттерди түзөбүз
# car1 = Car("Toyota", "ак")
# car2 = Car("BMW", "кара")

# # Методдорду колдонобуз
# car1.drive()  # Toyota унаасы жүрүп жатат!
# car2.drive()  # BMW унаасы жүрүп жатат!


# class car:
#     def __init__(self, model, color, year, price):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price

#     def sell (self):
#         return f"\033[36mi sell car: {self.model}\033[34m\ncolor: {self.color}\nyear:{2005} \nprice:{25000}\nБрат алсан окунбоойсун эркекче айтам"

# car1 = car("Mers","Blue",2005,25000)
# print(car1.sell())
# \033[31m-red 32-green 33-yellow 34-blue 35-purple 36-cian
# class footballplayer:
#     def __init__(self,name,age, national, club, position, goals = 0, assist = 0,trophies = 0):
#         self.name=name
#         self.age=age
#         self.national=national
#         self.club=club
#         self.position=position
#         self.goals=goals
#         self.assist=assist
#         self.trophies=trophies
#     def info(self):
#         return f"\033[036mname player-{self.name}\nage-{self.age}\nnation-{self.national}"
#     def static(self):
#         return f"\033[032mclub-{self.club}\nposition-{self.position}\ngoals-{self.goals}\nassist-{self.assist}\ntrophies-{self.trophies}"

# name = footballplayer("Cristiano Ronaldo", 40, "Portugal", "Al Nasr", "Forward", 950, 257, 36)
# print(name.info())
# print(name.static())




# class footballplayer:
#     def __init__(self,name,age, national, position, club1=0, club2=0, club3=0, club4=0, club5=0, club6=0, goals = 0, assist = 0,trophies = 0):
#         self.name=name
#         self.age=age
#         self.national=national
#         self.club1=club1
#         self.club2=club2
#         self.club3=club3
#         self.club4=club4
#         self.club5=club5
#         self.club6=club6
#         self.position=position
#         self.goals=goals
#         self.assist=assist
#         self.trophies=trophies
#     def info(self):
#         return f"\033[036mname player-{self.name}\nage-{self.age}\nnation-{self.national}"
#     def static(self):
#         return f"\033[032mposition-{self.position}\nclub1-{self.club1}\nclub2-{self.club2}\nclub3-{self.club3}\nclub4-{self.club4}\nclub5-{self.club5}\nclub6-{self.club6}\033[031m\ngoals-{self.goals}\nassist-{self.assist}\ntrophies-{self.trophies}"

# name = footballplayer("Cristiano Ronaldo", 40, "Portugal", "Forward", "Sporting 2002-2003", "Manchester United 2003-2009","Real Madrid 2009-2018", "Juwentus 2018-2021","Mancheester United 2021-2022", "Al Nasr 2023-2027", 950, 257, 36)
# print(name.info())
# print(name.static())

