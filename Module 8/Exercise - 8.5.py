class Point(object):  
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def __str__(self):
        return "(%s, %s)" % (str(self.x), str(self.y))

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Point(new_x, new_y)

p1 = Point(5, 3)
p2 = Point(2, 4)
p3 = p1 * p2

print(p1)
print(p2)
print(p3)