from project.band_members.musician import Musician


class Singer(Musician):
    SKILLS_AVAILABLE = ["sing high pitch notes", "sing low pitch notes"]

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.SKILLS_AVAILABLE:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."
