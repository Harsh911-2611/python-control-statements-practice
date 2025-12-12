# control_statements_practice_harsh.py
# Python Practice: Control Statements
# Author: Harsh Thakur
# This file contains 10 exercises demonstrating Python control statements.

# ----------------------------------------------
# 1. Check if a number is positive, negative, or zero
# ----------------------------------------------
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# ----------------------------------------------
# 2. Find the largest of three numbers
# ----------------------------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# ----------------------------------------------
# 3. Print all even numbers from 1 to 20
# ----------------------------------------------
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# ----------------------------------------------
# 4. Calculate factorial using while loop
# ----------------------------------------------
n = int(input("Enter a number to find its factorial: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial of", n, "is", fact)

# ----------------------------------------------
# 5. Demonstrate break and continue
# ----------------------------------------------
print("Demonstrating break and continue:")
for num in range(1, 11):
    if num == 5:
        continue  # skip 5
    if num == 9:
        break  # stop at 9
    print(num)

# ----------------------------------------------
# 6. Use pass statement
# ----------------------------------------------
print("Using pass statement:")
for i in range(1, 6):
    if i == 3:
        pass  # placeholder for future code
    else:
        print("Current number:", i)

# ----------------------------------------------
# 7. Nested if example
# ----------------------------------------------
num = int(input("Enter a number for nested if check: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")

# ----------------------------------------------
# 8. Print a simple triangle pattern
# ----------------------------------------------
print("Triangle pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# ----------------------------------------------
# 9. Print numbers divisible by both 3 and 5 between 1 and 50
# ----------------------------------------------
print("Numbers divisible by both 3 and 5:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# ----------------------------------------------
# 10. Find sum of digits of a number
# ----------------------------------------------
num = int(input("Enter a number to find sum of digits: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)
