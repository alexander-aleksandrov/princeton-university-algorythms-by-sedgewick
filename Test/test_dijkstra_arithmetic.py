import sys
sys.path.append('d:\\Projects\\princeton-university-algorythms-by-sedgewick')

from dijkstra_arithmetic_interpretator import evaluate
import pytest

@pytest.mark.parametrize("expression, expected", [
    ("(1+((2+3)*(4*5)))", 101), 
    ("(((1+2)*(3+4))+((5*6)*(7+8)))", 471), 
])

def test_evaluate(expression, expected):
    assert evaluate(expression) == expected