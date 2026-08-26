fruit = "apples" 
def pick_fruit():
    global fruit
    fruit = "oranges"
    return "I want some " + fruit 
print(pick_fruit())