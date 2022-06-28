# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------
from random import randint


class Warrior:
    def __init__(self, name, health=100, def_point=30, stamina=50):
        self.name = name
        self.health = health
        self.def_point = def_point
        self.stamina = stamina

    def hit(self, other):
        hit = 20
        print(f'{self.name} нанес урона {other.name} на {hit} очков.')
        other.health -= hit
        print(f'{other.name} осталось {other.health} здоровья.')

    def __str__(self):
        return f'{self.name}, {self.health} здоровья.'

    def attack(self, other):
        self.stamina -= 10
        hit_random = randint(0, 20)
        self.def_point -= randint(0, 10)

    def defence(self, other):
        pass


units = [Warrior("Ассасин"), Warrior("Тамплиер")]
gods_random = randint(0, 1)

while True:
    gods_random = not gods_random
    units[gods_random].hit(units[gods_random - 1])
    if units[gods_random - 1].health <= 0:
        winner = units[gods_random]
        break

print(f'\nПобедил {winner}')
