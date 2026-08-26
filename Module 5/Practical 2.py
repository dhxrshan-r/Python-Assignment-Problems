def ends_with(s, t):
    for i in range(len(t)):
        if s[len(s) - len(t) + i] != t[i]:
            return False
    return True
print(ends_with('Python', 'thon'))