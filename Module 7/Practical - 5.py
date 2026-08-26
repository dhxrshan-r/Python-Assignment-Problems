import copy

def complete_friendship(d):
    d_copy = copy.deepcopy(d)
    for name in d_copy:
        for friend in d_copy[name]:
            if friend not in d:
                d[friend] = set()
            d[friend].add(name)
    return d

d = {"alice": {"bob", "charlie"},
         "eve": {"alice"}}
print(complete_friendship(d))