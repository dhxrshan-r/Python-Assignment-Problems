def binary_search(L, target):      
    start = 0
    end = len(L) - 1           
    while(start <= end):
        middle = (start + end)//2
        if(L[middle] == target): 
            return True
        elif(L[middle] > target): 
            end = middle-1
        else: 
            start = middle+1
    return False

def is_intersecting1(L1, L2):
    for a in L1:
        if (a in L2):
            return True
    return False

def is_intersecting2(L1, L2):
    L2.sort()
    for a in L1:
        if (binary_search(L2, a)):
            return True
    return False

def is_intersecting3(S1, S2):
    for a in S1:
        if (a in S2):
            return True
    return False

import time

L1 = list(range(25*1000))[::-1]
L2 = list(range(25*1000, 50*1000))[::-1]

S1 = set(range(25*1000))
S2 = set(range(25*1000, 50*1000))

time_start = time.time()
is_intersecting1(L1, L2)
time_end = time.time()

print("Time for is_intersecting1 in seconds:", time_end - time_start)

time_start = time.time()
is_intersecting2(L1, L2)
time_end = time.time()

print("Time for is_intersecting2 in seconds:", time_end - time_start)

time_start = time.time()
is_intersecting3(S1, S2)
time_end = time.time()

print("Time for is_intersecting3 in seconds:", time_end - time_start)