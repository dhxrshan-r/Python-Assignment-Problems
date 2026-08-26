class Donut(object):
    def __init__(self, flavor):
        self.flavor = flavor
        self.filling = None
        self.sprinkles = False
    def fill_donut(self, filling):
        self.filling = filling
    def has_sprinkles(self):
        return self.sprinkles
    def sprinkle_donut(self):
        self.sprinkles = True
    def donut_info(self):
        if self.filling == None:
            print(self.flavor + " donut with no filling")
        else:
            print(self.flavor + "donut with" + self.filling + "filling")
d1 = Donut("vanilla")
print(d1.has_sprinkles())
d1.sprinkle_donut()
print(d1.has_sprinkles())
d1.donut_info() 