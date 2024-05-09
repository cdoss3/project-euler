#! /bin/python3

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

def linear_combination(a, b, c, d, e, f, g, h):
    """
    Return the sum of the linear combination to represent the sum of the coins
    """

    return 1*a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h

valid_combinations = []

for a in range(201):
    for b in range(101):
        for c in range(41):
            for d in range(21):
                for e in range(11):
                    for f in range(5):
                        for g in range(3):
                            for h in range(2):
                                if linear_combination(a, b, c, d, e, f, g, h) == 200:
                                    valid_combinations.append([a, b, c, d, e, f, g, h])

combos = len(valid_combinations)

print(f"Combinations: {combos}")
