import sys
sys.path.append("d:\\Projects\\princeton-university-algorythms-by-sedgewick\\")

from sorts import quick_sort
import random
import pytest

@pytest.mark.parametrize("arr", [[random.sample(range(100), 10) for _ in range(10)]])
def test_quick_sort(arr):
    for a in arr:
        quick_sort(a, 0, len(a)-1)
        assert a == sorted(a)
