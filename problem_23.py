"""

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""


def proper_divisors(num):
    """Return a list of proper divisors of input number"""
    divisors = []
    for k in range(1, (num // 2) + 1):
        if num % k == 0:
            divisors.append(k)
    if len(divisors) == 1:
        return None
    return divisors

def is_abundant(num):
    """Check for abundance in a number"""
    divisors = proper_divisors(num)
    total = 0
    if divisors is None:
        return False
    for divisor in divisors:
        total += divisor
    if total > num:
        return True
    return False


ab_list = []


for k in range(12, 28124):
    if k in ab_list:
        pass
    if is_abundant(k):
        print(f'{k} is abundant, adding to list')
        n = 2
        while n * k < 28124:
            if n * k in ab_list:
                n += 1 
            else:
                ab_list.append(n * k)
                print(f'{n * k} is an abundant multiple of {k}, adding to list')
                n += 1

ab_list.sort()

summable = []

for m in range(len(ab_list)):
    for n in range(m, len(ab_list)):
        current_sum = ab_list[m] + ab_list[n]
        if current_sum > 28124 or current_sum in summable:
            print("Sum too high, moving on")
            break
        else:
            summable.append(current_sum)
            print(f'{current_sum} is summable through {m} and {n}')


TOTAL = 0

for i in range(28124):
    if i not in summable:
        TOTAL += i

print(TOTAL)














"""ab_list = []

summable = []

for k in range(28123 // 2 + 1):
    if is_abundant(k):
        ab_list.append(k)
        summable.append(k)
    n = 2
    while k * n < 28123:
        if (k * n) not in summable:
            summable.append(k * n)


def is_sum_of_abundant(num):
    for ab in ab_list:
        for k in range(ab_list.index(ab), len(ab_list)):
            if ab + ab_list[k] == num:
                return True
            if ab_list[k] >= num:
                return False
    return False


final_list = []

for k in range(12, 28124):
    if is_sum_of_abundant(k):
        print(f'Passed {k}')
        pass
    elif k in ab_list:
        print(f'Passed {k}')
        pass
    else:
        print(f'Added {k}')
        final_list.append(k)

print(final_list)

big_sum = 0

for num in final_list:
    big_sum += num

print(big_sum)"""

"""for num in ab_list:
    for i in range(ab_list.index(num), len(ab_list)):
        summed_list.append(num + ab_list[i])

big_total = 0

for n in range(28124):
    if n not in summed_list:
        big_total += n

print(big_total)"""