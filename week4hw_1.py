# variables
item_price = 99
amount = 0
discount = 0
total_price = 0

# ask user for the number ordered
amount = int(input("How many would you like to purchase?\n"))

if (10 <= amount <= 19):
    discount = 0.1
elif (20 <= amount <= 49):
    discount = 0.2
elif (50 <= amount <= 99):
    discount = 0.3
elif (amount >= 100):
    discount = 0.4

print(f"The discount is {discount * 100}%")

total_price = amount * item_price * (1 - discount)

print(f"The total is ${total_price}.")