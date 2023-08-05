from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        musician_with_the_same_name = [m for m in self.musicians if m.name == name]
        if musician_with_the_same_name:
            raise Exception(f"{name} is already a musician!")
        new_musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_with_same_name = [b for b in self.bands if b.name == name]
        if band_with_same_name:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_with_same_place = [c for c in self.concerts if c.place == place]
        if concert_with_same_place:
            raise Exception(f"{place} is already registered for {genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = [m for m in self.musicians if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band[0].members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = [m for m in band[0].members if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band[0].members.remove(musician[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]

        desired_singer = [m for m in band.members if m.__class__.__name__ == "Singer"]
        desired_guitarist = [m for m in band.members if m.__class__.__name__ == "Guitarist"]
        desired_drummer = [m for m in band.members if m.__class__.__name__ == "Drummer"]
        #
        if not desired_singer or not desired_drummer or not desired_guitarist:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]

        if concert.genre == "Rock":
            if "sing high pitch notes" not in desired_singer[0].skills or \
                    "play the drums with drumsticks" not in desired_drummer[0].skills or \
                    "play rock" not in desired_guitarist[0].skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            if "sing low pitch notes" not in desired_singer[0].skills or \
                    "play the drums with drumsticks" not in desired_drummer[0].skills or \
                    "play metal" not in desired_guitarist[0].skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            if "sing high pitch notes" not in desired_singer[0].skills or "sing low pitch notes" not in desired_singer[0].skills or\
                    "play the drums with drum brushes" not in desired_drummer[0].skills or \
                    "play jazz" not in desired_guitarist[0].skills:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."



# musician_types = ["Singer", "Drummer", "Guitarist"]
# names = ["George", "Alex", "Lilly"]
#
# app = ConcertTrackerApp()
#
# for i in range(3):
#     print(app.create_musician(musician_types[i], names[i], 20))
#
# print(app.musicians[0].learn_new_skill("sing high pitch notes"))
# print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
# print(app.musicians[2].learn_new_skill("play rock"))
#
# print(app.create_band("RockName"))
# for i in range(3):
#     print(app.add_musician_to_band(names[i], "RockName"))
#
# print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.start_concert("Sofia", "RockName"))

