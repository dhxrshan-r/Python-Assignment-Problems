def strip(s):
    start = 0
    end = len(s) - 1
    for c in s:
        if c != ' ':
            break
        start += 1
    for c in reversed(s):
        if c != ' ':
            break
        end -= 1
    return s[start:end+1]
print(strip('   Hello World   '))