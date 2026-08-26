def all_subsets(S):
    if len(S) == 0:
        return [set()]
    T = S.copy()
    s = T.pop()
    subsets_without_s = all_subsets(T)
    subsets_with_s = []
    for A in subsets_without_s:
        A_copy = A.copy()
        A_copy.add(s)
        subsets_with_s.append(A_copy)
    return subsets_without_s + subsets_with_s

def max_clique(G):
    K = set(G)
    subsets = all_subsets(K)

    def is_clique(subset, friend):
        lst = list(subset)
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if not friend[lst[i]][lst[j]]:
                    return False
        return True
    
    max_set = set()
    length = 0
    for subset in subsets:
        if is_clique(subset, G) and len(subset) > length:
            length = len(subset)
            max_set = subset
    return max_set
    
G = {"Alice": {"Alice": True, "Bob": True, "Charlie": True},
     "Bob": {"Alice": True, "Bob": True, "Charlie": False},
     "Charlie": {"Alice": True, "Bob": False, "Charlie": True}}
print(max_clique(G))