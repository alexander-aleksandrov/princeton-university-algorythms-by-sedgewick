from UF import WeightedQuickUnionUF
from quiq_find import QF
import pytest

@pytest.fixture
def qu_20():
    qu = WeightedQuickUnionUF(20)
    qu.union(0, 1)
    qu.union(2, 3)
    qu.union(0, 2)
    qu.union(4, 5)
    return qu

@pytest.fixture
def qf_20():    
    qf = QF(20)
    qf.union(0, 1)
    qf.union(2, 3)
    qf.union(0, 2)
    qf.union(4, 5)
    return qf

@pytest.fixture
def qu_find_max_20():
    qu = WeightedQuickUnionUF(20)
    qu.union(1, 2)
    qu.union(2, 6)
    qu.union(9, 6)
    qu.union(4, 5)
    return qu


@pytest.fixture(params=["qf_20", "qu_20"])
def union_find_fixture(request):
    return request.getfixturevalue(request.param)

@pytest.mark.parametrize("a, b, expected", [
    (0, 1, True),
    (0, 2, True),
    (2, 3, True),
    (4, 5, True),
    (0, 4, False),
    (0, 5, False),
    (1, 2, True),
    (1, 3, True),
    (1, 4, False),
    (1, 5, False),
    (2, 4, False),
    (2, 5, False),
    (3, 4, False),
    (3, 5, False),
    (4, 0, False),
    (4, 1, False),
    (4, 2, False),
    (4, 3, False),
    (5, 0, False),
    (5, 1, False),
    (5, 2, False),
    (5, 3, False)
])
def test_union_find(union_find_fixture, a, b, expected):
    assert union_find_fixture.is_connected(a, b)==expected

@pytest.mark.parametrize("max, expected", [
    (1, 9),
    (2, 9),
    (6, 9),
    (4, 5),
    (7, 7)
])    
def test_find_max(qu_find_max_20, max, expected):
    assert qu_find_max_20.find_max(max)==expected