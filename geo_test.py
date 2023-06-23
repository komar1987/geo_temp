from geo import add 
from geo import subtract
from geo import devide

from geo import mean    # Saeb added this line

def test_add():
    assert add (13 , 17) == 30

def test_subtract():
    assert subtract (50 , 20) == 30

def test_devide():
    assert devide (70 , 10) == 7

# Saeb added this function
def test_mean():
    assert mean(1,2,3) == 2

    
