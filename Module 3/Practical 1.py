def n_once(n):
    result = 0
    for i in range(n):
        result += 10**i
    return result
print(n_once(5))