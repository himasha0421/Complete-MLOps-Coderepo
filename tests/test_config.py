"""define application test cases"""

import pytest


class NotInRange(Exception):
    def __init__(self, message="value not in range") -> None:
        self.message = message
        super().__init__(self.message)

def test_generic():
    """generic type test"""
    a=2
    b=2
    assert a == b

def test_range():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange