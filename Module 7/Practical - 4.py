def duplicated_ids(L):
    checked = set()
    duplicate = set()
    for d in L:
        if d["id"] in checked:
            duplicate.add(d["id"])
        else:
            checked.add(d["id"])
    return list(duplicate)
L =  [ {"id": 1, "major": "computer science", "gpa": 4},
       {"id": 2, "major": "mathematics", "gpa": 3.5},
       {"id": 3, "major": "chemical engineering", "gpa": 3.7} ]
print(duplicated_ids(L))