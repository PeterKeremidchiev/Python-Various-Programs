n = int(input())
set_of_names = set()

for _ in range(n):
    name = input()
    set_of_names.add(name)

print(*set_of_names, sep="\n")