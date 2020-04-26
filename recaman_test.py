import pytest
from recaman import calculate_racaman

def test_uniqeness():
    sequence = calculate_racaman(200)
    for elem in sequence:
        assert sequence.count(elem) == 1
    sequence = calculate_racaman(400)
    for elem in sequence:
        assert sequence.count(elem) == 1

def test_sequencelength():
    sequence = calculate_racaman(200)
    assert len(sequence) == 200
    sequence = calculate_racaman(42)
    assert len(sequence) == 42