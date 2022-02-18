#Future value calculator

# gather data
p = float(input("Enter the principal amount:\n"))
r = float(input("Enter the yearly investment percentage:\n"))
time = int(input("Enter the amount of time in years:\n"))

# convert the percentage into a decimal
r /= 100

# calculate the future value
output = p * (1 + r) ** time
output = round(output, 2)
print(f"The future value is ${output}")

