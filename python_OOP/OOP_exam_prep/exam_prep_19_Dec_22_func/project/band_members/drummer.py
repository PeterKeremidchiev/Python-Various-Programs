from project.band_members.musician import Musician


class Drummer(Musician):
    SKILLS_AVAILABLE = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.SKILLS_AVAILABLE:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."

# dr = Drummer("test", 20)
# dr.learn_new_skill("play the drums with drumsticks")
# dr.learn_new_skill("play the drums with drumsticks")
# print(dr.SKILLS_LEARNED)