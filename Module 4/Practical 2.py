def count_multiples_with_end_digit(n, digit):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            multiple = i*j
            if multiple % 10 == digit:
                count += 1
    return count
print(count_multiples_with_end_digit(6, 2))