n = int(input())
stack = []

for i in range(n):
    number_data = [int(x) for x in input().split()]
    command = number_data[0]

    if command == 1:
        stack.append(number_data[1])
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))
# new_stack = []
# while stack:
#     removed = stack.pop()
#     new_stack.append(removed)
# print(", ".join(new_stack))

stack.reverse()
print(*stack, sep=", ")