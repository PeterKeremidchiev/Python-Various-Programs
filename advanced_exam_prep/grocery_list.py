def shop_from_grocery_list(budget, products, *args):
    low_budget = False

    if products:
        if args:
            for arg in args:
                current_product_name = arg[0]
                product_price = arg[1]
                if current_product_name in products:
                    if product_price <= budget:
                        products.remove(current_product_name)
                        budget -= product_price
                    else:
                        low_budget = True
                        break
                else:
                    continue

    if low_budget and products:
        return f"You did not buy all the products. Missing products: {', '.join(products)}."
    if not products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    if budget and products:
        return f"You did not buy all the products. Missing products: {', '.join(products)}."


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "aggg", "meat"],
#     ("asd", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
print(shop_from_grocery_list(
    0,
    [],
    # ("colaaa", 15.00),
    # ("chocolate", 30),
    # ("tomato", 15.85),
    # ("chips", 50),
    # ("meat", 22.99),
))
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))
