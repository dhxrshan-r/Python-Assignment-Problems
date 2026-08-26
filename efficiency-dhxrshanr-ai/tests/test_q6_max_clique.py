from q6_max_clique import max_clique 

def test_max_clique():
    G = {"Alice": {"Alice": True, "Bob": True, "Charlie": True},
          "Bob": {"Alice": True, "Bob": True, "Charlie": False},
          "Charlie": {"Alice": True, "Bob": False, "Charlie": True}}
    assert(max_clique(G) == {"Alice", "Bob"} or max_clique(G) == {"Alice", "Charlie"})

    G1 = {"Tara": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True},
          "Sam": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True},
          "Ryan": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True},
          "Priya": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True}}
    assert(max_clique(G1) == {"Tara", "Sam", "Ryan", "Priya"})


