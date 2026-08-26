def nth_achilles_number(n):
    count = 0
    num = 0
    while count <= n:
        num += 1
        if is_powerful(num) and (not is_perfect_power(num)):
            count += 1
    return num

def is_powerful(x):
    if x < 1:
        return False
    elif is_prime(x):
        return False
    for factor in range(2, x):
        if x % factor == 0 and is_prime(factor):
            if x % (factor ** 2) != 0:
                return False
    return True

def is_prime(x):
    if x < 2:
        return False
    for factor in range(2, x):
        if x % factor == 0:
            return False
    return True

import math
def is_perfect_power(x):
    pow = 2
    root = x ** (1/pow)
    while round(root) > 1:
        if math.isclose(root, round(root)):
            return True
        pow += 1
        root = x ** (1/pow)
    return False
print(nth_achilles_number(1))