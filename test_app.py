import pytest
from app import calculer_puissance

def test_calculer_puissance():
    assert calculer_puissance(2, 3) == 8
    assert calculer_puissance(5, 0) == 1
    assert calculer_puissance(3, 4) == 81


