from q6_num_lines import num_lines 


def test_num_lines():
    s = "Hello world"
    assert(num_lines(s) == 1)
    s1 = """ Hello 
                world """
    assert(num_lines(s1) == 2)
    s2 = """    There are
            many lines
            here
            with
            spaces.   """
    assert(num_lines(s2) == 5)
