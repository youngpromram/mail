import pytest
value = set([2,5,6])
def test_chet():
    for x in value:
        assert x%2==0,'Четное число'
        assert x%2!=0,'Нечетное число'

def test_zero():
    try:
        assert 1/0
    except ZeroDivisionError:
        pass
    
def test_value():  
        assert len(value)!=0 ,'Пустой'
