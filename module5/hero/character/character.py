# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

from random import randint


class Character:
    """ Parent class """

    def __init__(self, name, health, mana, level):
        """ Initiate hero """
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    def show_hero(self):
        descriptrion = {'Name: ': self.name,
                        'Health: ': self.health,
                        'Mana: ': self.mana,
                        'Level: ': self.level
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
        # global critical

        def level_up():
            self.level += 1

        def critical():

            crit = randint(0, 3)
            return crit

        if damage == 0:
            print("Miss!")
        else:
            if critical() == 2:
                print(f'Крит - {critical()}.Нанесено {damage * critical()} урона.')
                # self.level += 1
                level_up()
            elif critical() == 3:
                print(f'Крит - {critical()}.Нанесено {damage * critical()} урона.')
                # self.level += 1
                level_up()
            else:
                print(f'Нанесено {damage} урона.')

    def move(self):
        """ Start moving """
        print(f'{self.name} start moving... ')


class Creep(Character):
    """ Child class """

    def __init__(self, name, health, mana, level, unit_type):
        """
        Первый init - указываем что будет в классе
        Второй init - какие параметры мы наследуем

        Основной косяк - нельзя (или я не понял как),
        наследовать параметры выборочно. Можно наследовать все,
        добавив что-то еще
        По этой приичне __init__ -> такой большой
        """
        super().__init__(name, health, mana, level)
        self.unit_type = unit_type

    def show_hero(self):
        descriptrion = {'Name: ': self.name,
                        'Health: ': self.health,
                        'Mana: ': self.mana,
                        'Level: ': self.level,
                        'Type: ':self.unit_type,
                        }
        print('----------------------')
        for specs in descriptrion:
            print(specs, descriptrion[specs])
        print('----------------------')
