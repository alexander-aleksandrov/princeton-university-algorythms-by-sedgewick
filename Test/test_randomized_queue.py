import pytest
from randomized_queue import RandomizedQueue    

@pytest.fixture
def empty_queue():
    return RandomizedQueue()    

@pytest.fixture
def queue_with_one_element():
    rq = RandomizedQueue()
    rq.enqueue(1)
    return rq

@pytest.fixture
def random_queue_with_five_elements():
    rq = RandomizedQueue()
    rq.enqueue(1)
    rq.enqueue(2)
    rq.enqueue(3)
    rq.enqueue(4)
    rq.enqueue(5)
    return rq

@pytest.mark.parametrize("queue_fixture, expected", [
    (pytest.lazy_fixture("empty_queue"), 0),
    (pytest.lazy_fixture("queue_with_one_element"), 1),
    (pytest.lazy_fixture("random_queue_with_five_elements"), 5)
])
def test_size(queue_fixture, expected):
    assert queue_fixture.size == expected

def test_dequeue_from_empty_queue(empty_queue):
    with pytest.raises(Exception):
        empty_queue.dequeue()

def test_sample_from_empty_queue(empty_queue):
    with pytest.raises(Exception):
        empty_queue.sample()

def test_dequeue_from_queue_with_one_element(queue_with_one_element):
    assert queue_with_one_element.dequeue() == 1
    assert queue_with_one_element.size == 0 

def test_sample_from_queue_with_one_element(queue_with_one_element):
    assert queue_with_one_element.sample() == 1
    assert queue_with_one_element.size == 1

def test_dequeue_from_random_queue_with_five_elements(random_queue_with_five_elements):
    x = random_queue_with_five_elements.dequeue()
    items = [1, 2, 3, 4, 5]
    assert x in items
    assert random_queue_with_five_elements.size == 4
    items.remove(x)
    x = random_queue_with_five_elements.dequeue()
    assert x in items
    assert random_queue_with_five_elements.size == 3

def test_iterator_random_queue_with_five_elements(random_queue_with_five_elements):
    items = [1, 2, 3, 4, 5]
    for item in random_queue_with_five_elements:
        assert item in items
        items.remove(item)
    assert len(items) == 0
    assert random_queue_with_five_elements.size == 5
