# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------
from character import Character
from character import Creep


hero1 = Character("Riki", 100, 40, 20)
hero1.show_hero()
hero1.get_damage(20)
hero1.attack(20)
hero1.move()

creep_radiant = Creep("Trebushet", 60, 0, 1, "creeps")
creep_radiant.show_hero()
