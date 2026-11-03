make = input("Enter auto make: ")
model = input("Enter auto model: ")
msrp = float(input("Enter MSRP: "))
discount_percent = float(input("Enter discount percent as a decimal (e.g. 0.10): "))

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print(f"Make: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrp:,.2f}")
print(f"Discount percent: {discount_percent:.2f}")
print(f"Amount off: ${amount_off:,.2f}")
print(f"Discounted price: ${discounted_price:,.2f}")