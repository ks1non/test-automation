from pytest import mark
import random
numbers = [1,2,3]
# @mark.smoke
def test_1():
    pass

@mark.ui
def test_2():
    pass

@mark.ui
@mark.smoke

def test_3():
    assert 1 == 1
