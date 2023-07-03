from inheritance_exercise.need_for_speed.project import Hero

class Elf(Hero):
    def __init__(self, username, level):
        Hero.__init__(self, username, level)
        Hero.__str__(self)