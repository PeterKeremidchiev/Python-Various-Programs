n = int(input())
set_odd = set()
set_even = set()

for i in range(1, n + 1):
    name = input()
    sum_of_integers = sum(list([ord(x) for x in name]))
    divide = sum_of_integers // i
    if divide % 2 == 0:
        set_even.add(divide)
    else:
        set_odd.add(divide)
if sum(set_odd) > sum(set_even):
    # sorted_set = sorted(set_odd, reverse=True)
    print(*set_odd.difference(set_even), sep=", ")
elif sum(set_even) > sum(set_odd):
    print(*set_even.symmetric_difference(set_odd), sep=", ")
elif sum(set_even) == sum(set_odd):
    print(*set_even.union(set_odd), sep=", ")


