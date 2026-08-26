def intersect(L, K):
    s = set(L)
    result = []
    for value in K:
        if value in s:
            result.append(value)
    return result
L = [1, 2, 2, 3, 0]
K = [1, 1, 2, 5, 0]
print(intersect(L, K))