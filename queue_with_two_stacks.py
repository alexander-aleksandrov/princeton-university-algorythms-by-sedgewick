class QueueWithTwoStacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            raise Exception("Queue is empty")

        return self.stack2.pop()