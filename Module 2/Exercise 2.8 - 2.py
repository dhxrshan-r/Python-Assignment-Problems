def roll_dice(p1, r1, p2, r2):
    if r1 >= r2:
        return p1
    else:
        return p2
print(roll_dice(2,7,5,9))