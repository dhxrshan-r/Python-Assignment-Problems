def count_apples(name, num_apples="zero"):
    sentence = name + " has " + num_apples + " apples."
    return sentence
print(count_apples("Ben")) 
print(count_apples("Christine", "three"))