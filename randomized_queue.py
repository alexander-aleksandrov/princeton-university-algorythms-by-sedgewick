import random

class RandomizedQueue:
    def __init__(self):
        self._array = [None]
        self._deleted_places = []
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    @property
    def size(self):
        return self._size
    
    def enqueue(self, item):
        if item == None:
            raise Exception("Item is None")
        if len(self._deleted_places) > 0:
            self._array[self._deleted_places.pop()] = item
        if self._tail == len(self._array):
            self._array += [None] * len(self._array)
        self._array[self._tail] = item
        self._tail += 1
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("RandomizedQueue is empty")
        index = random.randint(0, self._tail-1)
        while self._array[index] is None:
            index = random.randint(0, self._tail-1)
        self._deleted_places.append(index)
        item = self._array[index]
        self._array[index] = None
        self._size -= 1
        return item

    def sample(self):
        if self.is_empty():
            raise Exception("RandomizedQueue is empty")
        return self._array[random.randint(0, self._tail-1)]

    def __iter__(self):
        return self.RandomizedQueueIterator(self)
    
    class RandomizedQueueIterator:
        def __init__(self, queue):
            self._array = queue._array
            self._indices = [i for i, item in enumerate(self._array) if item is not None]
            self._size = queue._size
        def __next__(self):
            if not self._indices:
                raise StopIteration
            index = random.choice(self._indices)
            self._indices.remove(index)
            return self._array[index]
        def __iter__(self):
            return self
