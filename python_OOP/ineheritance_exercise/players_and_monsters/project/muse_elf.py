from inheritance_exercise.need_for_speed.project import Elf

class MuseElf(Elf):
    def __init__(self, username, level):
        Elf.__init__(self, username, level)