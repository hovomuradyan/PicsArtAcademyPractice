def price_counter_small(a):
  return a * 0.1

def price_counter_big(a):
  return a * 0.25

small_count = int(input())
big_count = int(input())
price = price_counter_small(small_count) + price_counter_big(big_count)
print("$" + str(price))
