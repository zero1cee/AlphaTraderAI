capital = int(input("Enter the capital amount: "))
risk = int(input("Enter the risk percentage: "))
stop_loss = int(input("Enter the stop loss amount: "))

risk_amount = capital * (risk / 100)


print("Capital: " , capital)
print("Risk Amount : ", risk_amount)