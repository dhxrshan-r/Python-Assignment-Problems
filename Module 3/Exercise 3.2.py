def sum_of_even(n):
    total = 0
    count = 1
    while count <= n** 2:
        if count % 2 == 0:
            total += count
        count += 1
    return total
print(sum_of_even(10))
