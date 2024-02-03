# twosided queue
class Deque:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            self.prev = None

    def is_empty(self):
        return self._first == None

    @property
    def size(self):
        return self._size

    def add_first(self, item):
        if item == None:
            raise Exception("Item is None")
        self._size += 1
        if self.is_empty():
            self._first = self.Node(item)
            self._last = self._first
        else:
            old_first = self._first
            self._first = self.Node(item)
            self._first.next = old_first
            old_first.prev = self._first
    
    def add_last(self, item):
        if item == None:
            raise Exception("Item is None")
        self._size += 1
        if self.is_empty():
            self._last = self.Node(item)
            self._first = self._last
        else:
            old_last = self._last
            self._last = self.Node(item)
            self._last.prev = old_last
            old_last.next = self._last

    def remove_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        self._size -= 1
        item = self._first.item
        if self._first.next is None:
            self._first = None
            self._last = None
        else:
            self._first = self._first.next
            self._first.prev = None
        return item
        
    def remove_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        self._size -= 1
        item = self._last.item
        if self._last.prev is None:
            self._last = None
            self._first = None
        else:
            self._last = self._last.prev
            self._last.next = None
        return item

    def __iter__(self):
        return self.DequeIterator(self)
    
    class DequeIterator:
        def __init__(self, deque):
            self._current = deque._first
        def __iter__(self):
            return self
        def has_next(self):
            return self._current.next != None
        def __next__(self):
            if self._current is None:
                raise StopIteration
            item = self._current.item
            self._current = self._current.next
            return item
