def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    result = []

    def place_kid():
        if len(kids) == 1:
            if behaviour == "Nice":
                nice_list.append(kids[0][1])
            else:
                naughty_list.append(kids[0][1])
            santa_list.remove(*kids)

    for arg in args:
        number, behaviour = arg.split("-")
        kids = [info for info in santa_list if info[0] == int(number)]
        place_kid()
    for name, behaviour in kwargs.items():
        kids = [info for info in santa_list if info[1] == name]
        place_kid()

    if nice_list:
        result.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        result.append(f"Naughty: {', '.join(naughty_list)}")
    if santa_list:
        result.append(f"Not found: {', '.join(x[1] for x in santa_list)}")

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
 [
 (7, "Peter"),
 (1, "Lilly"),
 (2, "Peter"),
 (12, "Peter"),
 (3, "Simon"),
 ],
 "3-Nice",
 "5-Naughty",
 "2-Nice",
 "1-Nice",
 ))
