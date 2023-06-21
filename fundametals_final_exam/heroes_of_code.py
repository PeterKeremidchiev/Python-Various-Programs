n = int(input())
heroes = {}

for i in range(n):
    hero = input().split(" ")
    name = hero[0]
    hit = int(hero[1])
    mana = int(hero[2])
    heroes[name] = {"hit": hit, "mana": mana}

command = input()

while command != "End":
    line = command.split(" - ")
    action = line[0]

    if action == "CastSpell":
        name = line[1]
        mana_needed = int(line[2])
        spell = line[3]
        if heroes[name]["mana"] >= mana_needed:
            heroes[name]["mana"] -= mana_needed
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['mana']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif action == "TakeDamage":
        name = line[1]
        damage = int(line[2])
        attacker = line[3]
        heroes[name]["hit"] -= damage
        if heroes[name]["hit"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hit']} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")

    elif action == "Recharge":
        name = line[1]
        amount = int(line[2])

        if heroes[name]["mana"] > 200:
            continue
        else:
            diff = abs(200 - heroes[name]["mana"])
            heroes[name]["mana"] += amount
            if heroes[name]["mana"] > 200:
                heroes[name]["mana"] = 200
            if amount > diff:
                print(f"{name} recharged for {diff} MP!")
            else:
                print(f"{name} recharged for {amount} MP!")

    elif action == "Heal":
        name = line[1]
        amount = int(line[2])
        if heroes[name]["hit"] > 100:
            continue
        else:
            diff = abs(100 - heroes[name]["hit"])
            heroes[name]["hit"] += amount
            if heroes[name]["hit"] > 100:
                heroes[name]["hit"] = 100
            if amount > diff:
                print(f"{name} healed for {diff} HP!")
            else:
                print(f"{name} healed for {amount} HP!")

    command = input()

for key, value in heroes.items():
    print(f"{key}\n HP: {heroes[key]['hit']}\n MP: {heroes[key]['mana']}")