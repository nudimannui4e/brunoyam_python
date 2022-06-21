# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

import random


class Character:

    def __init__(self, name, health, mana, level):
        """ Initiate hero """
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    def show_hero(self):
        descriptrion = {'Name': self.name,
                        'Health': self.health,
                        'Mana': self.mana,
                        'Spells': self.spells,
                        'Level': self.level
                        }
        print('----------------------')
        for specs in descriptrion:
            print(specs, descriptrion[specs])
        print('----------------------')

    def get_damage(self, damage=0):

        self.health -= damage
        print(f'Получен урон {damage}. Осталось {self.health} ед.з.')

    def level_up(self):
        self.level += 1

    def attack(self, damage=0):
        #global critical

        def level_up():
            self.level += 1

        def critical():
            crit = random.randint(0, 3)
            return crit

        if damage == 0:
            print("Miss!")
        else:
            if critical() == 2:
                print(f'Крит - {critical()}.Нанесено {damage * critical()} урона.')
                #self.level += 1
                level_up()
            elif critical() == 3:
                print(f'Крит - {critical()}.Нанесено {damage * critical()} урона.')
                #self.level += 1
                level_up()
            else:
                print(f'Нанесено {damage} урона.')