def num_odd_digits(n):
    n = abs(n)
    count = 0
    while n>0:
        digit = n % 10
        if digit % 2 == 1:
            count += 1
        n //= 10
    return count
print(num_odd_digits(123456789))