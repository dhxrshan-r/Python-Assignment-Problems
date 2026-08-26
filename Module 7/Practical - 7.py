#without using binary search

def Lower_index(L, target):
    for i in range(len(L)):
        if L[i] == target:
            return i
    return -1

def higher_index(L, target):
    for i in range(len(L) - 1, -1, -1):
        if L[i] == target:
            return i
    return -1

def index_range(L, target):
    first = Lower_index(L, target)
    last = higher_index(L, target)
    return [first, last]

L = [3, 5, 5, 6, 7, 8, 8, 8]
print(index_range(L, 8))

#using binary search

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

def lower_index(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        if L[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return start

def higher_index(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        if L[middle] <= target:
            start = middle + 1
        else:
            end = middle - 1
    return end

def index_range(L, target):
    if not binary_search(L, target):
        return [-1, -1]
    return [lower_index(L, target), higher_index(L, target)]

print(index_range([3, 5, 5, 6, 7, 8, 8, 8], 8))