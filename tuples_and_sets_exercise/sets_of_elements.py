n = [int(x) for x in input().split()]
first_set = set()
second_set = set()

for i in range(sum(n)):
    num = int(input())
    if i < n[1]:
        first_set.add(num)
    else:
        second_set.add(num)

print(*first_set.intersection(second_set), sep="\n")





