# variables
weight = 0
rate = 0

# user input
weight = float(input("How much does the package weigh?\n"))


if (weight <= 2.0):
    rate = 1.5
elif (2.0 < weight <= 6.0):
    rate = 3.0
elif (6.0 < weight <= 10.0):
    rate = 4.0
elif (weight > 10.0):
    rate = 4.75


rate = format(rate, ".2f")
print(f"The shipping rate is ${rate}")
