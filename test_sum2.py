#!/usr/bin/python3

def test_sum():
    assert sum([1,2,3]) == 6, "Should be equal to 6"

def test_tuple():
    assert sum([1,1,9]) == 6, "Should be equal to 6"
    

if __name__ == "__main__":
    test_sum()
    test_tuple()
    print("Everthing passed")
