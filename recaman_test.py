import pytest
from recaman import calculate_racaman

def test_uniqeness():
    sequence = calculate_racaman(200)
    for elem in sequence:
        assert sequence.count(elem) == 1