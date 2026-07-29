# Fuel Cost Calculator

distance = float(input("Enter the distance to be traveled (in km): "))
fuel_cost_per_litre = float(input("Enter the fuel cost per litre: "))
fuel_needed = float(input("Enter the fuel needed (in litres): "))
total_fuel_cost = fuel_cost_per_litre * fuel_needed
print(f"Total Fuel Cost: ₦{total_fuel_cost:,.2f}")