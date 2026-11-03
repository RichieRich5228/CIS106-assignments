ticker = input("Enter stock ticker symbol: ").upper()
shares = int(input("Enter number of shares: "))
cost_per_share = float(input("Enter cost per share: "))

amount_invested = shares * cost_per_share

print(f"Ticker: {ticker}")
print(f"Amount invested: ${amount_invested:.2f}")
