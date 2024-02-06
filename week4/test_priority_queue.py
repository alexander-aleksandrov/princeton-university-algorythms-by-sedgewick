from priority_queue import MaxPQ
from priority_queue import MinPQ
import random
import pytest

@pytest.fixture
def empty_pq():
    return MaxPQ()

@pytest.fixture
def pq():
    pq = MaxPQ()
    for i in range(10):
        pq.insert(random.randint(0, 100))
    return pq

@pytest.fixture
def pq_sorted():
    pq = MaxPQ()
    for i in range(10):
        pq.insert(i)
    return pq

@pytest.fixture
def min_pq():
    return MinPQ()

@pytest.fixture
def min_pq_sorted():
    pq = MinPQ()
    for i in range(10):
        pq.insert(i)
    return pq

def test_insert_min(min_pq):
    min_pq.insert(10)
    assert len(min_pq) == 1
    assert min_pq.pop() == 10
    assert len(min_pq) == 0

def test_pop_min(min_pq_sorted):
    assert len(min_pq_sorted) == 10
    min_pq_sorted.pop()
    assert len(min_pq_sorted) == 9

def test_peek_min(min_pq):
    min_pq.insert(100)
    assert min_pq.peek() == 100

def test_sort_min(min_pq_sorted):
    min_pq_sorted.sort()
    for i in range(10):
        assert min_pq_sorted.pop() == i

def test_insert(empty_pq):
    empty_pq.insert(10)
    assert len(empty_pq) == 1
    assert empty_pq.pop() == 10

def test_pop(pq):
    assert len(pq) == 10
    pq.pop()
    assert len(pq) == 9

def test_peek(pq):
    pq.insert(100)
    assert pq.peek() == 100

def test_sort(pq_sorted):
    pq_sorted.sort()
    for i in range(1, 10, -1):
        assert pq_sorted.pop() == i    