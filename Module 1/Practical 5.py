def compute_total(total, tax):
    final = total + total*tax
    print("Your total is " + str(final) + " dollars.")
    return final
print(compute_total(12, 0.05))