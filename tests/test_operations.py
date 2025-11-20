from src.math import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert subtract(-1, 1) == -2