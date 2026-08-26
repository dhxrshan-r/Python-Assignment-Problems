def most_factors(x, y):
    large_num = 0
    large_factors = []
    for num in range(x, y + 1):
        current_factors = get_prime_factors(num)
        if large_num is 0:
            large_num = num
            large_factors = current_factors
        if len(current_factors) > len(large_factors):
            large_num = num
            large_factors = current_factors
        elif len(current_factors) == len(large_factors):
            if sum_factors(current_factors) > sum_factors(large_factors):
                large_num = num
                large_factors = current_factors
    print(sorted(large_factors))
    return large_num


def get_prime_factors(x):
    factors = []
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            factors.append(divisor)
            x = x // divisor  
        else:
            divisor = divisor + 1           
    return factors


def sum_factors(factor_list):
    total = 0
    for factor in factor_list:
        total += factor
    return total
print(most_factors(100, 110)) 