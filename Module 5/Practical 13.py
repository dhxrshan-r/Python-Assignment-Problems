def insert_list(L, i, K):
    len_L = 0
    for value in L:
        len_L += 1
    result = []
    for _ in range(len_L - i):
        last_value = L[-1]
        result = [last_value] + result
        del L[-1] 
    L += K
    L += result
    return None

L = [1, 5, 6]
K = [6, 3, 4]
print(insert_list(L, 1, K))