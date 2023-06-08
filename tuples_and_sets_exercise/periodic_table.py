n = int(input())
# set_of_elements = set([el for el in input().split()] for i in range(n))
set_of_elements = set()
for i in range(n):
    elements = input().split()
    for el in elements:
        set_of_elements.add(el)
#     set_of_elements = set([el for el in elements])
#
print(*set_of_elements, sep="\n")
