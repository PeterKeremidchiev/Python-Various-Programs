from inheritance_exercise.need_for_speed.project import Knight

class DarkKnight(Knight):
    def __init__(self, username, level):
        Knight.__init__(self, username, level)