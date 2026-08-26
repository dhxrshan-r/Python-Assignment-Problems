""" Question 1: average_of_max_scores """
"""
Input: 2D list representing students and scores
Output: average of max scores across all students
"""
def average_of_max_scores(data):
    d=dict()
    for user,score in data:
        if user not in d: #d.get(user,0)==0:
            d[user]=score
        else:
            d[user]=max(d[user],score)
    total = sum(d.values())
    num = len(d)
    return total/num

""" Test 1 """
def test_average_of_max_scores():
    print("Testing average_of_max_scores...", end='')
    L = [["alice", 70], ["bob", 70], ["alice", 80], ["charlie", 90]]
    assert(average_of_max_scores(L) == 80)
    L1 = [["david", 50], ["david", 88], ["david", 79]]
    assert(average_of_max_scores(L1) == 88)
    L2 = [["elena", 100], ["fiona", 100]]
    assert(average_of_max_scores(L2) == 100)
    print("... done!")

if __name__ == '__main__':
    test_average_of_max_scores()