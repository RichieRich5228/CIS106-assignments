fixed_costs = float(input("Enter the fixed costs: "))
price_per_unit = float(input("Enter the price per unit: "))
cost_per_unit = float(input("Enter the cost per unit: "))

break_even = fixed_costs / (price_per_unit - cost_per_unit)

print("Break-even point (units to sell):", break_even)