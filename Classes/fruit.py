class Fruit:
    def __init__(self,color,taste,name):
        self.color = color
        self.taste = taste
        self.name = name
    def ripe_fruits(self):
        return f"Winnie bought a {self.color},{self.taste},{self.name}"
    def fresh_fruits(self):
        return f"I am a {self.taste},{self.name}"
    def pack_fruits(self):
        return f"I am an expensive pack of {self.color},{self.taste},{self.name}"
