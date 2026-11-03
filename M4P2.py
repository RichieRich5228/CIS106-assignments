purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = int(input("Enter the quantity of stock: "))

change = (current_price - purchase_price) * quantity

print("Change in value:", change)