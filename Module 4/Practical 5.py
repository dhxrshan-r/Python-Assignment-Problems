def recursive_sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return (n % 10) + recursive_sum_digits(n // 10)
print (recursive_sum_digits(1345))