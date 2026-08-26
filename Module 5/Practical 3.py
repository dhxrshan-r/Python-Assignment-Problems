def starts_with(s, t, start):
    if s[start :start+ len(t)] == t:
        return True
    return False

#from q1_starts_with import starts_with 

def find(s, t, start):
    for i in range(start, len(s)):
        if starts_with(s,t,i):
            return i
    return -1 

print (find("Hello world", "wor", 2))