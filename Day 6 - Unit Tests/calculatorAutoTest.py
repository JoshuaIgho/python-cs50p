#python3 -m pip install pytest - that's how to install pytest 
from calculator import square 

def testPositive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(5) == 25

def testNegative():
    assert square(-2) == 4
    
def testZero():
    assert square(0) == 0


#instead of python3, we will use pytest for testing