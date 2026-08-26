def nth_fibonacci_number(n):
    phi = (1 + 5**0.5) / 2
    conj = 1 - phi
    return round((phi**n - conj**n) / (5**0.5))
print(nth_fibonacci_number(7))