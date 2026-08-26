def merge_dicts(L):
    merge_dicts = dict()
    for s in L:
        for key, value in s.items():
            if key not in merge_dicts:
                merge_dicts[key] = value
            else:
                if isinstance(merge_dicts[key], set):
                    merge_dicts[key].add(value)
                elif merge_dicts[key] != value:
                    merge_dicts[key] = {merge_dicts[key], value}
    return merge_dicts
L = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 7, "c": 3}, {"a": 3, "b": 9, "c": 10}]
print(merge_dicts(L))

#other method
def merge_dicts(L):
    merge_dicts = dict()
    for d in L:
        for key, value in d.items():
            if key not in merge_dicts:
                merge_dicts[key] = value
            elif value != merge_dicts[key]:
                if not isinstance(merge_dicts[key], set):
                    merge_dicts[key] = {merge_dicts[key]}
                merge_dicts[key].add(value)
    return merge_dicts
L = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 7, "c": 3}, {"a": 3, "b": 9, "c": 10}]
print(merge_dicts(L))