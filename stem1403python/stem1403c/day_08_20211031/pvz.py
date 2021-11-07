"""
[Homework]
Date: 2021-10-24
Due date: 2021-10-30
1. Write code for your game system in OO
Create at least 3 instances (objects) of plant
Create at least 3 instances (objects) of zombie
Note that more than one type for both plant and zombie instances are supposed to be created.
Describe the battle process between a peashooter and a zombie and write down as a comment
Write some trial code to implement that process in sequence.
Hints:
Coding strictly according to your design (the description of battle process)
Submit your code including your description of the battle process

"""

import time

zombie_total = 3  # global variable
sunflower = 50  # global variable


class SnowPea:
    def __init__(self, posx, posy):
        self.name = "Snow pea"
        self.color = "White"
        self.hp = 120
        self.height = 120
        self.shot_distance = 7
        self.posx = posx
        self.posy = posy

    #  adding methods
    def shoot(self):
        print(f"{self.name} is shooting")

    def getHurt(self):
        self.hp -= 20
        if self.hp == 0:
            self.die()

    def die(self):
        return "Snow pea is died"


class PotatoMine:
    def __init__(self, posx, posy):
        self.name = "PotatoMine"
        self.color = "Brown"
        self.hp = 120
        self.height = 5
        self.posx = posx
        self.posy = posy

    #  adding methods
    def detect(self):
        if PoleVaultingZombie.eat() and NormalZombie.eat() and FlagZombie.eat():
            self.explode()

    def explode(self):
        print(f"The {self.name} is explode")
        self.hp = 0


class Sunflower:
    def __init__(self, posx, posy):
        self.name = "Sunflower"
        self.color = "Yellow"
        self.hp = 120
        self.height = 120
        self.posx = posx
        self.posy = posy

    #  adding methods
    def provide(self):
        global sunflower
        print(f"{self.name} is provide the sunflower's money")
        time.sleep(2)
        sunflower += 20
        print(f"You have {sunflower} sunflower")

    def getHurt(self):
        self.hp -= 20
        if self.hp == 0:
            self.die()

    def die(self):
        return f"{self.name} is died"


class NormalZombie:
    def __init__(self, posx, posy):
        self.name = "Normal Zombie"
        self.color = "NormalColor"
        self.hp = 120
        self.height = 120
        self.speed = 5
        self.hair = False
        self.clothing = "NormalClothing"
        self.posx = posx
        self.posy = posy

    #  adding methods
    def eat(self, plant):
        print(f"The {self.name} is eating {plant}")
        plant.getHurt()

    def move(self):
        print(f"{self.name} is moving")

    def getHurt(self):
        self.hp -= 20
        print("Normal Zombie is get hurt, hp-20")
        if self.hp == 0:
            global zombie_total
            print("One normal Zombie is dead")
            zombie_total -= 1
            print(f"You have {zombie_total} to kill.")


class FlagZombie:
    def __init__(self, posx, posy):
        self.name = "Flag Zombie"
        self.color = "NormalColor"
        self.hp = 120
        self.height = 120
        self.speed = 5
        self.hair = False
        self.clothing = "NormalClothing"
        self.posx = posx
        self.posy = posy

    #  adding methods
    def eat(self, plant):
        print(f"The {self.name} is eating {plant}")
        plant.getHurt()

    def move(self):
        print(f"{self.name} is moving")

    def hold(self):
        pass

    def getHurt(self):
        self.hp -= 20
        print(f"{self.name} is get hurt, hp-20")

        if self.hp == 0:
            self.die()

    def die(self):
        global zombie_total
        print(f"One {self.name} is dead")
        zombie_total -= 1
        print(f"You have {zombie_total} to kill.")


class PoleVaultingZombie:
    def __init__(self, posx, posy):
        self.name = "Pole Vaulting Zombie"
        self.color = "NormalColor"
        self.hp = 120
        self.height = 120
        self.speed = 5
        self.hair = False
        self.clothing = "NormalClothing"
        self.posx = posx
        self.posy = posy

    #  adding methods
    def eat(self, plant):
        print(f"The {self.name} is eating {plant}")
        plant.getHurt()

    def move(self, speed):
        print(f"The {self.name} is moving")

    #
    # def hold(self):
    #     pass

    def getHurt(self):
        self.hp -= 20
        print(f"{self.name} is get hurt, hp-20")
        if self.hp == 0:
            self.die()

    def die(self):
        global zombie_total
        print(f"One {self.name} Zombie is dead")
        zombie_total -= 1
        print(f"You have {zombie_total} to kill.")


class Bullet:
    def __init__(self, dmg=20):
        self.dmg = dmg

    def __str__(self):
        return f"dmg={self.dmg}"


# hp = 120
# height = 120
# color = "NormalZombieColor"
# shot_number = 6


putNormalZombie = NormalZombie(8, 7)

putNormalZombie.move()

print("First element you can put while be Sunflower to provide more sunflower's money.")
putSunflower = Sunflower(1, 7)
putSunflower.provide()

print("Now, you can put the Snowpea to shot")
putSnowPea = SnowPea(2, 7)
print("Snow pea is in 2, 7")
for i in range(3):
    putNormalZombie.move()
    putSnowPea.shoot()
    putNormalZombie.getHurt()
time.sleep(1)
putFlagZombie = FlagZombie(8, 6)
print("Another Zombie is coming...")
print("Oh no, you have anything in range 6")
print("You need to put something")
print("Maybe another Snowpea")
putSnowPea_2 = SnowPea(2, 6)

putSunflower.provide()

for i in range(2):
    putNormalZombie.move()
    putSnowPea.shoot()
    putNormalZombie.getHurt()
    # print(putNormalZombie.hp)

putSunflower.provide()

putFlagZombie.move()
time.sleep(3)
for i in range(2):
    print()
    putSnowPea_2.shoot()
    putFlagZombie.getHurt()

putNormalZombie.move()
putSnowPea.shoot()
putNormalZombie.getHurt()

for i in range(4):
    print()
    putSnowPea_2.shoot()
    putFlagZombie.getHurt()

putSunflower.provide()

print("The last Zombie is coming")
time.sleep(1)
putPoleVaultingZombie = PoleVaultingZombie(8, 7)
for i in range(6):
    print()
    putSnowPea.shoot()
    putPoleVaultingZombie.getHurt()

print("Ok Finally you killed all the zombies. Good job! ")

bullet1 = Bullet()
bullet2 = Bullet(40)

