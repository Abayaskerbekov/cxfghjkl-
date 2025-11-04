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

# 2 DZ


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

# 2 DZ 


# name = {
#     "abdu" : 18,
#     "from" : "Kyrgyzstan",
#     "city" : "bishkek",
#     "real city" : "manas"
# }

# print(name["from"])


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



""" S """
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report: {self.data}"

class ReportSaver:
    def save(self, report, filename):
        with open(filename, "w") as f:
            f.write(report.generate())

""" O """
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class RegularDiscount(Discount):
    def calculate(self, price):
        return price * 0.9  # 10% скидка

class VIPDiscount(Discount):
    def calculate(self, price):
        return price * 0.8  # 20% скидка

def get_final_price(discount: Discount, price):
    return discount.calculate(price)


""" L """
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def swim(self):
        print("Swimming")

""" I """
class Workable:
    def work(self): pass

class Eatable:
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self): print("Human working")
    def eat(self): print("Human eating")

class Robot(Workable):
    def work(self): print("Robot working")

""" D """
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

# Использование:
email_sender = EmailSender()
notif = Notification(email_sender)
notif.notify("Hello SOLID!")
