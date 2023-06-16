def shopping_cart(*args):
    meals = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for arg in args:
        meal = arg[0]
        product = arg[1]
        if arg == "Stop":
            break

        elif meal == "Pizza" and len(meals["Pizza"]) < 4:
            if product not in meals["Pizza"]:
                meals["Pizza"].append(product)

        elif meal == "Soup" and len(meals["Soup"]) < 3:
            if product not in meals["Soup"]:
                meals["Soup"].append(product)

        elif meal == "Dessert" and len(meals["Dessert"]) < 2:
            if product not in meals["Dessert"]:
                meals["Dessert"].append(product)

    for value in meals.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''

    for tuple_ in sorted_meals:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    'Stop',
    ('Pizza', 'mushrooms'),
))






