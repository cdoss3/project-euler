"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

# Define a function to return a list of the proper divisors of an integer 'num'. Return None for prime numbers

def proper_divisors(num):
    divisors = []

    for k in range(1, (num // 2) + 1):
        if num % k == 0:
            divisors.append(k)
    
    if len(divisors) == 1:
        return None
    
    return divisors

def amicable_test(num1, num2):
    # If either number is prime, abort
    if proper_divisors(num1) == None or proper_divisors(num2) == None or num1 == num2:
        return False
    else:
        sum1 = 0
        sum2 = 0

        for number in proper_divisors(num1):
            sum1 += number
        for number in proper_divisors(num2):
            sum2 += number

        if sum1 == num2 and sum2 == num1:
            return True
        else:
            return False


def sum_list(number_list):
    total = 0
    if number_list != None:
        for number in number_list:
            total += number

    return total


def find_amicables(n):
    pair_list = []

    for k in range(4, n):
        divisor_sum = sum_list(proper_divisors(k))
        if amicable_test(k, divisor_sum) and (k not in pair_list) and (divisor_sum not in pair_list):
            pair_list.append(k)
            pair_list.append(divisor_sum)
    
    return pair_list

final_pairs = find_amicables(10000)
print(final_pairs)
print(sum_list(final_pairs))
