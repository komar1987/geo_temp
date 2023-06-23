from geo import add 
from geo import subtract
from geo import devide

from geo import add_three_value   # Saeb added this line

def test_add():
    assert add (13 , 17) == 30

def test_subtract():
    assert subtract (50 , 20) == 30

def test_devide():
    assert devide (70 , 10) == 7

# Saeb aded this function 
def test_add_three_value ():
    assert add_three_value (10, 20, 30) == 60
