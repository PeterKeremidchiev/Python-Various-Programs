class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.starting_num = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.starting_num -= 1
        if self.starting_num < 0:
            raise StopIteration
        return self.starting_num

iterator = countdown_iterator(0)
for item in iterator:
 print(item, end=" ")