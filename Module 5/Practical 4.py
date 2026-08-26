#method 1

def starts_with(s, t, start):
    if s[start :start+ len(t)] == t:
        return True
    return False

def count(s, t):
    count = 0
    for i in range(len(s) - len(t)):
        if starts_with(s,t,i):
           count += 1
    return count
print(count("hello", "l") == 2)

#method 2

def starts_with(s, t, start):
    if s[start :start+ len(t)] == t:
        return True
    return False

def count(s, t):
    count = 0
    start = 0
    while start < len(s):
        if starts_with(s,t,start):
           count += 1
           start += len(t)
        else:
           start += 1
    return count
print(count("aaaaa", "aa"))