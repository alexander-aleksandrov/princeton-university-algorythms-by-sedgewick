import random

class RandomizedQueue:
    def __init__(self):
        self._array = [None]
        self._tail = 0
    def is_empty(self):
        return len(self._array) == 0

    def size(self):
        return len(self._array)
    
    def enqueue(self, item):
        if self._tail == len(self._array):
            self._array += [None] * len(self._array)
        self._array[self._tail] = item
        self._tail += 1

    def dequeue(self):
        return self._array.pop(random.randint(0, len(self._array) - 1))

    def sample(self):
        return self._array[random.randint(0, len(self._array) - 1)]

    def __len__(self):
        return len(self._array)

    def __iter__(self):
        return iter(self._array)
