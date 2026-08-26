from q1_average_of_max_scores import average_of_max_scores 

def test_average_of_max_scores():
    L = [["alice", 70], ["bob", 70], ["alice", 80], ["charlie", 90]]
    assert(average_of_max_scores(L) == 80)
    L1 = [["david", 50], ["david", 88], ["david", 79]]
    assert(average_of_max_scores(L1) == 88)
    L2 = [["elena", 100], ["fiona", 100]]
    assert(average_of_max_scores(L2) == 100)

