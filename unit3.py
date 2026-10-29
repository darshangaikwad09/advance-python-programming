
import json
with open("products.json", "r") as file:
    products = json.load(file)

total = 0

for p in products:
    value = p["Quantity"] * p["price"]
    print(p["Product"], "=", value)
    total += value

print("Total value of all products =", total)
