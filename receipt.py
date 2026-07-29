# Restaurant Receipt
"""
Customer Name
Product
Price
Quantity
Then calculate:
Total = Price × Quantity

Display:
MISS MUFFINS
Customer: Cornelius
Product: Meat Pie
Price: ₦1,500
Quantity: 4
Total: ₦6,000
Thank you.
"""
name = input("Customer's name: ").title().strip()
product = input("Product: ").title().strip()
price = float(input("Price: "))
qty = int(input("Quantity: "))
total = price*qty

print(f"Customer's name: {name}\nProduct: {product}\nPrice: {price}\nQuantity: {qty}")
print(f"Total: N{total}")
print("Thank you for your patronage")