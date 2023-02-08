#!/usr/bin/python3
# a test case script

def test_sum():
    # function to check the sum of numbers

    assert sum([1,2,3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything has passed")
