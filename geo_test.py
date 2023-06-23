from geo import add 
from geo import subtract
from geo import devide
from geo import multiply

def test_add():
    assert add (13 , 17) == 30

def test_subtract():
    assert subtract (50 , 20) == 30

def test_devide():
    assert devide (70 , 10) == 7

def test_multiply():
    assert multiply(10 , 11 , 2) == 220
    