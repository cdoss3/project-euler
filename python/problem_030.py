#! /bin/python3

def fifth_power_sum(num):
    """
    Deconstruct a number into its digits. Then sum the fifth powers of those digits
    and return the value of that sum

    num -> int
    """
    # Track the sum
    sum = 0

    # Loop through all digits of a given number, add the sum of the fifth power to the sum
    for digit in str(num):
        sum += int(digit) ** 5

    return sum

# Collect all the sums of the fifth powers into one list
fifth_powers = []

for n in range(10, 1000000):
    """
    Go through enough numbers to try and collect all cases of a number's fifth powers
    summing to the original number
    """
    if n == fifth_power_sum(n):
        fifth_powers.append(n)

print(f"All fifth powers: {fifth_powers}")

final_sum = 0

for k in fifth_powers:
    final_sum += k

print(f"Sum of all numbers that can be written as the sum of the fifth powers of their digits is {final_sum}")

