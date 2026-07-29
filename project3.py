# Restaurant Receipt

name = input("Customer's name: ").title().strip()
product = input("Product: ").title().strip()
price = float(input("Price: "))
qty = int(input("Quantity: "))
total = price*qty

print(f"Customer's name: {name}\nProduct: {product}\nPrice: {price}\nQuantity: {qty}")
print(f"Total: N{total}")
print("Thank you for your patronage")
