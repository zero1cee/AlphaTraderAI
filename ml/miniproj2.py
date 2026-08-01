price = int(input("Enter the current price of gold: "))

if price > 3400:
         print("Strong Buy")

elif 3400 > price > 3350:
         print("Buy")

elif 3350 > price > 3300:
         print("Hold")

elif 3300 > price:
         print("Sell")
