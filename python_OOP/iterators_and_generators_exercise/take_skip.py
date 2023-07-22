class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = -self.step
        self.count_nums = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count_nums += 1
        self.start += self.step
        if self.count_nums > self.count:
            raise StopIteration
        return self.start



numbers = take_skip(10, 5)
for number in numbers:
 print(number)