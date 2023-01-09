child_meal_price = float(input("What is the price of a child's meal? "))

adult_meal_price = float(input("what is the price of an adult's meal? "))

drink_price = float(input("Soda price: "))

appetizers_price = float(input("Appetizers price: "))

drinks = int(input("How many drinks? "))

appetizers = int(input("How many appetizers? "))

children = int(input("How many children are there? "))

adult = int(input("How many adults are there? "))

sales_tax = float(input("What is the sales tax rate? "))

print()

sideMenuPrice1 = int(drink_price * drinks)

sideMenuPrice2 = int(appetizers_price * appetizers)

totalSideMenuPrice = sideMenuPrice1 + sideMenuPrice2

total_meal_price_child = int(child_meal_price * children)

total_meal_price_adult = int(adult_meal_price * adult)

subTotal = total_meal_price_child + total_meal_price_adult + totalSideMenuPrice

salesAfterTax = sales_tax * subTotal / 100

total = subTotal + salesAfterTax

print(f"Subtotal: ${subTotal:.2f}")

print(f"Sales tax: ${salesAfterTax:.2f}")

print(f"Total: ${total:.2f}")

print()

payment = float(input("What is the payment amount? "))

print(f"Change: ${payment - total:.2f}")