def is_anagram1(L1,L2):
    if len(L1) != len(L2):
        return False
    for num in L1:
        if L1.count(num) != L2.count(num):
            return False
    return True

L1 = list(range(25*1000))[::-1]
L2 = list(range(25*1000, 50*1000))[::-1]

print(is_anagram1(L1, L2))

import time
time_start = time.time()
is_anagram1(L1,L2)
time_end = time.time()
print("Time for is_anagram1 in seconds:", time_end - time_start)