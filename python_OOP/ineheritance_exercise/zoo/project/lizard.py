from inheritance_exercise.need_for_speed.project import Reptile


class Lizard(Reptile):
    def __init__(self, name: str):
        Reptile.__init__(self, name)