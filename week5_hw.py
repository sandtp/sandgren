# <question 1>

name = input("What is your name?\n")
nchances = 0
achances = 0
while not name.isalpha():
    name = input("What is your name?\n")
    nchances += 1
    if nchances == 2:
        print("Unacceptable")
        break

age = (input("How old are you?\n"))

while not age.isdigit():
    age = (input("How old are you?\n"))
    achances += 1
    if achances == 2:
        print("Unacceptable")
        break

if age.isdigit() and name.isalpha():
    print("Acceptable!")

#<\question 1>

#<question 2>
special_chars = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
passwd = input("Enter a password: \n")

# boolean variables for each condition:
length = False
upper = False
lower = False
digit = False

valid = False

while not valid:

# checks length of passwd
    if len(passwd) < 8:
        print("Your password must be more than 8 characters.")
        length = False
    else:
        length = True

# checks passwd for uppercase letters
    for char in passwd:
        if char.isupper():
            upper = True
            break
        upper = False

    if not upper:
        print("Your password needs an uppercase letter.")

# checks passwd for lowercase letters
    for char in passwd:
        if char.islower():
            lower = True
            break
        lower = False

    if not lower:
        print("Your password needs a lowercase letter.")

# checks passwd for numbers
    for char in passwd:
        if char.isdigit():
            digit = True
            break
        digit = False

    if not digit:
        print("Your password needs a number")

# checks passwd for special characters
    for char in passwd:
        if char in special_chars:
            special = True
            break
        special = False

    if not special:
        print("Your password needs a special character")

# checks if all conditions have been met
    if length == upper == lower == digit == special == True:
        print("Your password has been set")
        valid = True
    else:
        passwd = input("Enter a password: \n")

#<\question 2>

#<question 3>


for x in range(1, 1000):
    num = str(x)
    if num.isdigit():
        if "3" in num:
            print(num, end = " | ")

#<\question 3>
print("\n")
#<question 4>

sum = 0
for x in range(1, 10000):
    for i in str(x):
        sum += int(i)
    if sum == 17:
        print(x, end = " | ")
    sum = 0
#<\question 4>
print("\n")
#<question 5>

sum = 0
for x in range(1, 10000):
    num = str(x)
    if "3" in num:
        for i in str(x):
            sum += int(i)
        if sum == 23:
            print(x, end=" | ")
        sum = 0

#<\question 5>
print("\n")
#<question 6>

num = 100

while num >= 1:
    if num % 2 == 0:
        print(num, end = " | ")
    num -= 1

#<\question 6>
print("\n")
#<question 7>



for num in range(100, 1001):
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# I spent three hours of my time for one tab of whitespace.
#pain