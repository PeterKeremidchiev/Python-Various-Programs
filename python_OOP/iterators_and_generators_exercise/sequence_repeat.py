class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start_idx = -1
        # self.count = 0

    def __iter__(self):
        return self

    # def __next__(self):
    #     self.start_idx += 1
    #     self.count += 1
    #     if self.count > self.number:
    #         raise StopIteration
    #     if self.start_idx > len(self.sequence) - 1:
    #         self.start_idx = 0
    #     return self.sequence[self.start_idx]

    def __next__(self):
        if self.start_idx == self.number - 1:
            raise StopIteration

        self.start_idx += 1
        return self.sequence[self.start_idx % len(self.sequence)]


result = sequence_repeat('I Love Python', 3)
for item in result:
 print(item, end ='')