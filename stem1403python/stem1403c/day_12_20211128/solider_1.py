class Gun:
    def __init__(self, model):
        self.model = model
        self.capacity = 8
        self.bullet_count = self.capacity


    def add_bullet(self, count):
        self.bullet_count += count
        if self.bullet_count >= self.capacity:
            self.bullet_count = count
        print("The gun has been reloaded")

    def shoot(self):
        if self.bullet_count >= 1:
            self.bullet_count -= 1
            print(f"The {self.model} shot.")
        else:
            print(f"Reload!")


class Solider:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        Gun.shoot()


gun1 = Gun("AK47")

so1 = Solider("Solider", gun1)
gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()
gun1.shoot()



