class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.items = list(self.dictionary.items())
        self.start_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx >= len(self.items) - 1:
            raise StopIteration
        self.start_idx += 1

        return self.items[self.start_idx]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
 print(x)