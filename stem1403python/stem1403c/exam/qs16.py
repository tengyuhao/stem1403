class Computer:
    def __init__(self, CPU, memory, storage, wifi, graphic_card, ethernet):
        self.cpu = CPU
        self.memory = memory
        self.storage = storage
        self.wifi = wifi
        self.graphic = graphic_card
        self.ethernet = ethernet

    def on(self):
        pass

    def off(self):
        pass

    def run(self, program):
        pass

    def connect(self, wifi, ethernet):
        pass

    def __str__(self):
        return f"CPU={self.cpu}, memory={self.memory}, storage={self.storage}, wifi={self.wifi}, graphic card={self.graphic}, ethernet={self.ethernet}"


com1 = Computer("Intel i7 CPU", "2 x 8GB DDR3", "1TB SSD", True, "NVidia graphic card GeForce RTX 3090", True)
print(com1)
