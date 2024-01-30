class QU:
    def __init__(self, n):
        self.components = [i for i in range(n)]
        
    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        if self.find(a) != self.find(b):
            self.components[a]  = self.components[b]

    def find(self, a):
        while a != self.components[a]:
            a = self.components[a]
        return a 
    
if __name__ == '__main__':
    main()