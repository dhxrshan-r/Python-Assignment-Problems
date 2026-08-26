def getSlope(x1, y1, x2, y2):
    rise = y2-y1 
    run = x2-x1
    slope = rise/run 
    return slope 
print(getSlope(1, 4, 3, 2))
