def is_anagram1(L1,L2):
    if len(L1) != len(L2):
        return False
    for num in L1:
        if L1.count(num) != L2.count(num):
            return False
    return True

print(is_anagram1([1,2,3,4],[1,2,3,4]))

import time
time_start = time.time()
is_anagram1([1,2,3,4],[1,2,3,4])
time_end = time.time()
print("Time for is_anagram1 in seconds:", time_end - time_start)

# using dictionaries

def is_anagram2(L3,L4):
    if len(L3) != len(L4):
        return False
    count = dict()
    for num in L3:
        current_count = count.get(num, 0)
        count[num] = current_count + 1       
    for num in L4:
        count[num] -= 1
        if count[num] < 0:
            return False
    return True

time_start = time.time()
is_anagram2([1,2,3,4],[1,2,3,3])
time_end = time.time()
print("Time for is_anagram2 in seconds:", time_end - time_start)


def is_anagram3(L5,L6):
    if len(L5) != len(L6):
        return False
    d1 = dict()
    d2 = dict()
    for i in L5:
        count = d1.get(i,0)
        count += 1
        d1[i] = count

    for j in L6:
        count = d2.get(j,0)
        count += 1
        d2[j] = count

    return d1 == d2

time_start = time.time()
is_anagram3([1,2,3,4,5],[1,2,3,3,3])
time_end = time.time()
print("Time for is_anagram3 in seconds:", time_end - time_start)