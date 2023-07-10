import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.__create_matrix()
        self.current_row = 0

    def __create_matrix(self):
        matrix = []
        for i in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.current_row]) == 4:
            if self.current_row + 1 < self.pages:
                self.current_row += 1
            else:
                return "No more free slots"

        self.photos[self.current_row].append(label)
        return f"{label} photo added successfully on page " \
               f"{self.current_row + 1} slot " \
               f"{self.photos[self.current_row].index(label) + 1}"

    def display(self):
        res = ''
        for row in self.photos:
            res += "-----------\n" + f"{' '.join('[]' for photo_name in row)}\n"
        res += "-----------"
        return res


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))

print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
