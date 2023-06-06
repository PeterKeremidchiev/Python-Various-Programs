first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

# for i in range(n):
#     first_command, second_command, *data = input().split()
#     command = first_command + " " + second_command
#
#     if command == "Add First":
#         [first_set.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second_set.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first_set.discard(int(el)) for el in data]
#     elif command == "Remove Second":
#         [second_set.discard(int(el)) for el in data]
#     else:
#         print(first_set.issubset(second_set) or second_set.issubset(first_set))
#
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")

functions = {
    "Add First": lambda x: [first_set.add(el) for el in x],
    "Add Second": lambda x: [second_set.add(el) for el in x],
    "Remove First": lambda x: [first_set.discard(el) for el in x],
    "Remove Second": lambda x: [second_set.discard(el) for el in x],
    "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
}
for i in range(n):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command

    functions[command]([int(x) for x in data])

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
