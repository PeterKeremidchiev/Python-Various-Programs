def solution():
    def integers():
        integer = 1
        while True:
            yield integer
            integer += 1


    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for i in range(n)]

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))