class reverse_iter:
    def __init__(self, sequence):
        self.sequence = sequence
        self.start_idx = len(self.sequence)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start_idx -= 1
        if self.start_idx < self.end:
            raise StopIteration()
        return self.sequence[self.start_idx]





reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)