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
        self.role = 0

    def __str__(self):
        return f'{self.name}, {self.health} здоровья.'

    def defence(self):
        if self.def_point > 0:
            self.health -= randint(0, 20)
            self.def_point -= randint(0, 10)
        else:
            self.health -= randint(10, 30)

    def fight(self, other):
        if (self.role == 0) and (other.role == 0):
            return
        if (self.role == 0) and (other.role == 1):
            self.defence()
            return
        if (self.role == 1) and (other.role == 0):
            other.defence()
            return
        if (self.role == 1) and (other.role == 1):
            self.stamina -= randint(10, 30)
            self.health -= randint(10, 30)
            other.stamina -= randint(10, 30)
            other.health -= randint(10, 30)


units = [Warrior("Ассасин"), Warrior("Тамплиер")]

while True:
    for unit in units:
        print(unit)
        if unit.health <= 10:
            print(f'\nУмер {unit.name}')
            exit(0)
        unit.role = randint(0, 1)  # attack =1, def = 0
        if unit.role == 1:
            print(f'\n {unit.name} атакует')
    units[0].fight(units[1])