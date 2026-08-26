def number_bills_needed(cost):
    num_twenty = cost // 20
    cost = cost - num_twenty * 20
    num_five = cost // 5
    cost = cost - num_five * 5
    num_one = cost
    return num_twenty + num_five + num_one
print(number_bills_needed(42))