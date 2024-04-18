# Kieran Seven


class Dog:
    def __init__(self, name, trick, breed, hungry):
        self.name = name
        self.trick = trick
        self.breed = breed
        self.hungry = hungry

    def __str__(self):
        return self.name + ": " + self.breed

    def speak(self):
        print("Woof")

    def feed(self):
        self.hungry = False

    def change_trick(self, new_trick):
        self.trick = new_trick

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_trick(self):
        return self.trick

    def isHungry(self):
        return self.hungry
