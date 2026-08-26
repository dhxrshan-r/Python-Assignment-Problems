def remove_zeros(n):
    result = 0
    mul = 1

    while n > 0:
        digit = n % 10
        n //= 10

        if digit != 0:
            result += digit * mul
            mul *= 10

    return result
print(remove_zeros(10201))
