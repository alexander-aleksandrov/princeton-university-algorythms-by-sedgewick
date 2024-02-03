from deque import Deque
import pytest

@pytest.fixture
def empty_deque():
    return Deque()

@pytest.fixture
def deque_with_one_item():
    deque = Deque()
    deque.add_first(1)
    return deque

@pytest.fixture
def deque_with_two_items():
    deque = Deque()
    deque.add_first(1)
    deque.add_last(2)
    return deque

@pytest.fixture
def deque_with_three_items():
    deque = Deque()
    deque.add_first(1)
    deque.add_last(2)
    deque.add_first(3)
    return deque

@pytest.mark.parametrize("deque_fixture, expected", [
    (pytest.lazy_fixture("empty_deque"), 0),
    (pytest.lazy_fixture("deque_with_one_item"), 1),
    (pytest.lazy_fixture("deque_with_two_items"), 2)
])
def test_size(deque_fixture, expected):
    assert deque_fixture.size == expected

def test_first_remove(empty_deque):
    with pytest.raises(Exception):
        empty_deque.remove_first()

def test_latr_remove(empty_deque):
    with pytest.raises(Exception):
        empty_deque.remove_last()

def test_first_remove_one_item(deque_with_one_item):
    assert deque_with_one_item.remove_first() == 1
    assert deque_with_one_item.size == 0          

def test_last_remove_one_item(deque_with_one_item):
    assert deque_with_one_item.remove_last() == 1
    assert deque_with_one_item.size == 0

def test_first_remove_two_items(deque_with_two_items):
    assert deque_with_two_items.remove_first() == 1
    assert deque_with_two_items.size == 1    

def test_last_remove_two_items(deque_with_two_items):
    assert deque_with_two_items.remove_last() == 2
    assert deque_with_two_items.size == 1

def test_iter(empty_deque):
    with pytest.raises(Exception):
        next(iter(empty_deque))

def test_iter_one_item(deque_with_one_item):
    items = [i for i in deque_with_one_item]
    assert items == [1]
        
def test_iter_two_items(deque_with_two_items):
    items = [i for i in deque_with_two_items]
    assert items == [1, 2]

def test_iter_three_items(deque_with_three_items):
    items = [i for i in deque_with_three_items]
    assert items == [3, 1, 2]