def main():

    num1 = float(input("Enter the first number to be averaged:\n"))
    num2 = float(input("Enter the second number to be averaged:\n"))
    print("Average:")
    avg(num1, num2)

    input("Press enter to proceed")

    starting_num = int(input("Enter the starting number:\n"))
    ending_num = int(input("Enter the ending number:\n"))
    print("Result:")
    total_sum(starting_num, ending_num)

    input("Press enter to proceed")

    item_price = float(input("Enter the price of the item:\n"))
    percent_off = float(input("Enter the percent off:\n"))
    tax = float(input("Enter the tax in percent:\n"))
    print("Total price:")
    total_cost(item_price, percent_off, tax)

    input("Press enter to proceed")

    number = int(input("Enter a number:\n"))
    print("Result:")
    prime(number)

    input("Press enter to proceed")

    coprime_test = int(input("Enter a number to see its coprimes:\n"))
    print("Result:")
    print(coprime(coprime_test))

    input("Press enter to proceed")

    number_of_coprimes = int(input("Enter a number to see how many coprimes it has:"))
    print("Result:\n")
    coprime_count(number_of_coprimes)

def avg(first, second):

    average = (first + second) / 2
    print(average)

def total_sum(first, last):

    sum = 0
    for i in range (first, last + 1):

        sum = sum + i

    print(sum)
    

def total_cost(item_price, percent_off, tax):

    percent_off_fixed = percent_off / 100
    tax_fixed = tax / 100
    price_with_discount = item_price - (item_price * percent_off_fixed)
    total_price = price_with_discount + (price_with_discount * tax_fixed)
    print("{:,.2f}".format(total_price))

def prime(num):
    for x in range(0, num + 1):

        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                print(x)

def coprime(num):

    hcf = 0
    coprimes = []
    for x in range(2, num + 1):
        mn = min(num, x)
        for i in range(1, mn + 1):
            if num % i == 0 and x % i == 0:
                hcf = i
        if hcf == 1:
            coprimes.append(x)
    return coprimes

def coprime_count(num):

    print(len(coprime(num)))

def twinprimes(num):
    primes = []
    twinprimes = []
    for x in range(0, num + 1):

        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                primes.append(x)
    for x in primes:
        if x + 2 in primes:
            twinprimes.append(x, x + 2)





main()