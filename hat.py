import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

        @classmethod
    def sort(self, name):
        print(name, "is in", random.choice(cls.houses))

hat.sort("Harry")