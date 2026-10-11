food_bought = float(input("How many plates of food did you buy?: "))
price_per_food = float(input("How much was each plate of food?: "))
tip_amount = int(input("How much percent of tip would you like to give?: "))

def bill_amount(food, price, tip):
  if tip == 0:
    total_bill = (food * price)
  else:
    total_bill = (food * price) + tip/100*(food * price)
  return total_bill

total_bill_price = bill_amount(food_bought, price_per_food, tip_amount)
rounded_total = round(total_bill_price, 2)
print(rounded_total)