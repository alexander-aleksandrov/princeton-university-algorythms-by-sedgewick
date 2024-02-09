class RBBST():
    class Node():
        def __init__(self, key, value, color):
            self.key = key
            self.value = value
            self.color = color
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == 'red'

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 'red'
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 'red'
        return x

    def flip_colors(self, h):
        h.color = 'red'
        h.left.color = 'black'
        h.right.color = 'black'

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = 'black'

    def _put(self, h, key, value):
        if h is None:
            return self.Node(key, value, 'red')
        if key < h.key:
            h.left = self._put(h.left, key, value)
        elif key > h.key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value

        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)

        return h

    def get(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None

    def delete(self, key):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = 'red'
        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = 'black'

    def _delete(self, h, key):
        if key < h.key:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and h.right is None:
                return None
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)
            if key == h.key:
                x = self.min(h.right)
                h.key = x.key
                h.value = x.value
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self.balance(h)

    def _move_red_left(self, h):
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h
    