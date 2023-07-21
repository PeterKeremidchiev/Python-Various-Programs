class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        # self.vowel = [v for v in self.string if v.lower() in self.vowels]
        self.start_idx = -1
        self.end = len(self.string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_idx += 1
        if self.start_idx > self.end:
            raise StopIteration
        if self.string[self.start_idx].lower() in self.vowels:
            return self.string[self.start_idx]
        return self.__next__()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)