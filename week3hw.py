#present value calculator

# gather data
fv = float(input("Enter the future value\n"))
rate = float(input("Enter the yearly interest rate percentage\n"))
time = float(input("Enter the amount of time in years\n"))


# convert the percentage into a decimal
rate /= 100

# calculate the principal amount
p = fv / (1 + rate) ** time
p = round(p, 2)
# output
print(f"You need to invest ${p} in order to have ${fv} in {time} years.")
