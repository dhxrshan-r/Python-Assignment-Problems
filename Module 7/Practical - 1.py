def average_of_max_scores(data):
    max_scores = dict()
    for name, score in data:
        if name not in max_scores or score > max_scores[name]:
            max_scores[name] = score
            average = sum(max_scores.values()) / len(max_scores)
    return average
L = [["alice", 70], ["bob", 70], ["alice", 80], ["charlie", 90]]
print(average_of_max_scores(L))