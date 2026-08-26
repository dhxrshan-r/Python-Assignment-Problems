def starts_with(s,t,start):
    if s[start: len(t) + start] == t:
        return True
    return False

def find(s,t,start):
    for i in range(start, len(s)):
        if starts_with(s,t,i):
            return i
    return -1
print(find("world", "rld" , 1))