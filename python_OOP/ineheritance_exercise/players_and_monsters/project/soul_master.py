from inheritance_exercise.need_for_speed.project import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        DarkWizard.__init__(self, username, level)
