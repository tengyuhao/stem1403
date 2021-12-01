class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0
        self.capacity = 8

    def add_bullet(self):
        if self.bullet_count == self.capacity:
            print("This gun must be reloaded")
        else:
            self.shoot()

    def shoot(self):
        self.bullet_count += 1

    def reload(self, bullet_add):
        if self.bullet_count - bullet_add >= self.capacity:
            print("Too enough")
        else:
            print("reloaded")

class Solider:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):

        Gun.shoot()


gun1 = Gun("AK47", )
so1 = Solider("Solider", gun1)

