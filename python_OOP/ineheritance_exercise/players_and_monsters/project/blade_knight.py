from inheritance_exercise.need_for_speed.project import DarkKnight

class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        DarkKnight.__init__(self, username, level)

