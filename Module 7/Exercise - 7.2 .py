def has_repeats(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if (L[i] == L[j]):
                return True
    return False
print(has_repeats([1,2,3,4]))

#using sets

def has_repeats(L):
    s = set(L)
    if (len(s) != len(L)):
        return True
    return False
print(has_repeats([1,2,3,3]))