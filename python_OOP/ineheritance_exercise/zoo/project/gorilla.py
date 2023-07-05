from inheritance_exercise.need_for_speed.project import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        Mammal.__init__(self, name)
