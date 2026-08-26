from q5_complete_friendship import complete_friendship 

def test_complete_friendship():
    d = {"alice": {"bob", "charlie"},
         "eve": {"alice"}}
    res = {"alice": {"eve", "bob", "charlie"}, 
            "eve": {"alice"}, 
            "bob": {"alice"}, 
            "charlie": {"alice"}}
    assert(complete_friendship(d) == None)
    assert(d == res)

    d1 = {"frank": {"giselle", "karen"},
            "giselle": {"frank", "karen"},
            "karen": set()}
    res1 = {"frank": {"giselle", "karen"},
            "giselle": {"frank", "karen"},
            "karen": {"frank", "giselle"}}
    assert(complete_friendship(d1) == None)
    assert(d1 == res1)
    
