from inheritance_exercise.need_for_speed.project import Hero

class Wizard(Hero):
    def __init__(self, username, level):
        Hero.__init__(self, username, level)