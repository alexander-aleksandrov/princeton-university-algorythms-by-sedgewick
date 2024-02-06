class MaxPQ():
    def __init__(self):
        self._queue = [None]


    def swim(self, i):
        while i > 1 and  self._queue[int(i/2)] < self._queue[i]:
            self._queue[int(i/2)], self._queue[i] = self._queue[i], self._queue[int(i/2)]
            i = int(i/2)
        

    def sink(self, i):
        while 2*i <= len(self._queue):
            j = int(2*i)
            if  j < len(self._queue)-1 and self._queue[j] < self._queue[j+1]: 
                j += 1
            if self._queue[i] > self._queue[j]: 
                break

            self._queue[i], self._queue[j] = self._queue[j], self._queue[i]
            i = j

    def sort(self):
        for i in range(len(self._queue), -1):
            self.sink(i)


    def insert(self, a):
        self._queue.append(a)
        self.swim(len(self._queue)-1)
    
    def pop(self):
        if len(self._queue) == 1:
            return None
        if len(self._queue) == 2:
            return self._queue[1]
        else:
            item = self._queue[1]
            self._queue[1], self._queue[len(self._queue)-1] = self._queue[len(self._queue)-1], self._queue[1]
            self.sink(1)
            self._queue = self._queue[:-1]
            return item
    
    def peek(self):
        return self._queue[1]
    
    def __len__(self):
        return len(self._queue)-1
    
    def __str__(self):
        return str(self._queue)[1:]

class MinPQ():
    def __init__(self):
        self._queue = [None]


    def swim(self, i):
        while i > 1 and  self._queue[int(i/2)] > self._queue[i]:
            self._queue[int(i/2)], self._queue[i] = self._queue[i], self._queue[int(i/2)]
            i = int(i/2)
        

    def sink(self, i):
        while 2*i < len(self._queue):
            j = int(2*i)
            if  j + 1 < len(self._queue) and self._queue[j] > self._queue[j+1]: 
                j += 1
            if i < len(self._queue) and self._queue[i] <= self._queue[j]: 
                break

            self._queue[i], self._queue[j] = self._queue[j], self._queue[i]
            i = j

    def sort(self):
        for i in range(len(self._queue), -1):
            self.sink(i)


    def insert(self, a):
        self._queue.append(a)
        self.swim(len(self._queue)-1)
    
    def pop(self):
        if len(self._queue) == 1:
            return None
        if len(self._queue) == 2:
            item = self._queue[1]
            self._queue = self._queue[:-1]
            return item
        else:
            item = self._queue[1]
            self._queue[1], self._queue[len(self._queue)-1] = self._queue[len(self._queue)-1], self._queue[1]
            self._queue = self._queue[:-1]
            self.sink(1)
            return item
    
    def peek(self):
        return self._queue[1]
    
    def __len__(self):
        return len(self._queue)-1
    
    def __str__(self):
        return str(self._queue[1:])

def main():
    pq  = MinPQ()
    pq.insert(10)
    pq.pop()
    print(len(pq)) 


if __name__ == '__main__':  
    main()