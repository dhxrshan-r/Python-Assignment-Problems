def insert_element(L, i, el):
    len_L = 0
    for value in L:
        len_L += 1
    result = []
    for _ in range(len_L - i):
        last_value = L[-1]
        result = [last_value] + result
        del L[-1]
    L += [el]
    L += result
    print(L)    
L =  [1, 2, 3, 4]    
       
print((insert_element(L, 0, 5)))     