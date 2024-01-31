class QU:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]
        self.max_element = [i for i in range(n)]
        
    def is_connected(self, a, b):
        return self.root(a) == self.root(b)

    def union(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)
        if a_root != b_root:
            if self.sz[a_root] > self.sz[b_root]:
                self.id[b_root]  = self.id[a_root]
                self.sz[a_root] += self.sz[b_root]
                self.max_element[a_root] = max(self.max_element[a_root], self.max_element[b_root])
            else:
                self.id[a_root]  = self.id[b_root] 
                self.sz[b_root] += self.sz[a_root]
                self.max_element[b_root] = max(self.max_element[a_root], self.max_element[b_root])

    def find_max(self, a):
        return self.max_element[self.root(a)]            


    def root(self, a):
        root = a
        while root != self.id[root]:
            root = self.id[root]
        while a != root:
            next = self.id[a]
            self.id[a] = root
            a = next
        return a
    
if __name__ == '__main__':
    main()