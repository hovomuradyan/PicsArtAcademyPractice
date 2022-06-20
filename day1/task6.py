price = int(input("Please , input a price of product: "))
tip = price * 18/100
tax = (price - tip) * 20/100

print(f'price is {price}, tip is {tip}, tax is {tax}')
