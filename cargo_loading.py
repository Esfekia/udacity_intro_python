# Write a program that will add cargo to the ship
# as long as the total weight is not above 100kg.
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42),
            ("machine", 120), ("cheeses", 5)]
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    if weight >= 100:
        break
    elif cargo_weight+weight >= 100:
        continue
    else:
        items.append(cargo_name)
        weight += int(cargo_weight)

print(items)
print(weight)
