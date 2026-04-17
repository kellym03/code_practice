#Loops Practice
#Carly's clippers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price

average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
# print(new_prices)

new_total_prices = 0
for price in new_prices:
  new_total_prices += price

new_average_price = new_total_prices/len(new_prices)

print("New Average Haircut Price: " + str(new_average_price))

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# List of hairstyles under $30 after the price cut 
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles) - 1) if new_prices[i] < 30]
# the -1 is to avoid index error because range goes up to but does not include the last number and len(hairstyles) is 8 but the last index is 7.

print(cuts_under_30)
