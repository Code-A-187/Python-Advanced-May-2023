def shop_from_grocery_list(budget, list_, *prices):
    bought_items = []
    for product, price in prices:
        if product not in list_:
            continue
        else:
            if budget - float(price) < 0:
                break
            else:
                bought_items.append(product)
                list_.remove(product)
                budget -= float(price)
    if not list_:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(list_)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
