from inheritance_exercise.need_for_speed.project import Animal


class Mammal(Animal):
    def __init__(self, name: str):
        Animal.__init__(self, name)