from q9_get_averages_from_csv import get_averages_from_csv


def test_get_averages_from_csv():
    
    csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""
    assert(get_averages_from_csv(csv, "Number of Students") == 24719.75)
    assert(get_averages_from_csv(csv, "University") == None)
    assert(get_averages_from_csv(csv, "Tuition") == 68099.25)
    assert(get_averages_from_csv(csv, "Undergrad Population") == None)
    
