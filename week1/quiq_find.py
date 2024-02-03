class QF:
    def __init__(self, n):
        self.components = [i for i in range(n)]
        
    def is_connected(self, a, b):
        return self.components[a] == self.components[b]

    def union(self, a, b):
        a_component = self.components[a]
        b_component = self.components[b]
        for i in range(len(self.components)):
            if self.components[i] == a_component:
                self.components[i] = b_component    

    def find(self, a):
        return self.components[a]
    
    
    
if __name__ == '__main__':
    main()