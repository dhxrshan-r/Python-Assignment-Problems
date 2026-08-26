def num_lines(s):
    for c in s:
        if c == " ":
            s.splitlines(s)
    return len(s.splitlines(s))