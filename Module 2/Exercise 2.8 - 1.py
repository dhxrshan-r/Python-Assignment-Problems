def cost_to_mail(weight):
    if weight > 5:
        return 0.75 * (weight) + 5
    return 5
print(cost_to_mail(60))