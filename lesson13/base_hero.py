import random


import pyttsx3


class base_hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.engine=pyttsx3.init()

    def attack_others(self, other):
        damage = random.randint(1, self.attack)
        other.hp -= damage
        return f"{self.name} атакует {other.name} и наносит {damage}"

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"name: {self.name},hp: {self.hp}"

    def speak(self,other):
        text = f"i kil you {other.name}"
        self.engine.say(text)
        self.engine.runAndWait()


hero = base_hero("abdy",120, 50)
hero2 = base_hero("abdy", 10, 50)
print(hero.attack_others(hero2))
hero.speak(hero2)
print(hero2.is_alive())
