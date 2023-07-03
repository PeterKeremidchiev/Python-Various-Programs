from inheritance_exercise.need_for_speed.project import Wizard

class DarkWizard(Wizard):
    def __init__(self, username, level):
        Wizard.__init__(self, username, level)