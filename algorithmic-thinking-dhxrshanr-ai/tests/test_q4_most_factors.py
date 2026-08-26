from q4_most_factors import most_factors 


def test_most_factors():
    assert(most_factors(100, 110) == 108) # prints [2, 2, 3, 3, 3]
    assert(most_factors(50, 100) == 96) # prints [2, 2, 2, 2, 2, 3]
    assert(most_factors(20, 24) == 24) # prints [2, 2, 2, 3]
    assert(most_factors(40, 45) == 40) # prints [2, 2, 2, 5]
    assert(most_factors(37, 37) == 37) # prints [37]
