import matplotlib.pyplot as plt
import numpy as np
from UF import WeightedQuickUnionUF

class Percolation:
    def __init__(self, n):
        self._n = n
        self._qu = WeightedQuickUnionUF(n*n + 2)
        self._grid = [0 for i in range(n*n)]
        self._count = 0

    def id(self, row, col):
        return (row - 1) * self._n + (col - 1)

    def open(self, row, col):
        if not self.is_open(row, col):
            self._grid[self.id(row, col)] = 1
            self._count += 1
            self.check_neighbours(row, col)    

    def check_neighbours(self, row, col):
        if row == 1:
            self._qu.union(self.id(row, col) + 1, 0)
        if row == self._n:
            self._qu.union(self.id(row, col) + 1, self._n*self._n + 1)
        if row > 1 and self.is_open(row - 1, col):
            self._qu.union(self.id(row, col) + 1, self.id(row - 1, col) + 1)
        if row < self._n and self.is_open(row + 1, col):
            self._qu.union(self.id(row, col) + 1, self.id(row + 1, col) + 1)
        if col > 1 and self.is_open(row, col - 1):
            self._qu.union(self.id(row, col) + 1, self.id(row, col - 1) + 1)
        if col < self._n and self.is_open(row, col + 1):
            self._qu.union(self.id(row, col) + 1, self.id(row, col + 1) + 1)
        if col == 1 and self.is_open(row, col + 1):
            self._qu.union(self.id(row, col) + 1, self.id(row, col + 1) + 1)
        if col == self._n and self.is_open(row, col - 1):
            self._qu.union(self.id(row, col) + 1, self.id(row, col - 1) + 1)             

    def is_open(self, row, col):
        return self._grid[self.id(row, col)] == 1

    def is_full(self, row, col):
        if self.is_open(row, col):
            return self._qu.is_connected(0, self.id(row, col)+1)

    def percolates(self):
        return self._qu.is_connected(0, self._n*self._n + 1)
    
    def __str__(self):
        for i in range(self._n*self._n):
            print(self._grid[i], end=" ")
            if (i + 1)% self._n == 0:
                print()
        return ""
    

    @property
    def grid(self):
        return self._grid
    
    
    @property
    def count(self):
        return self._count   
    

# draws a percolation system using Matplotlib when percolates() == True
def draw_grid(p):
    fig, ax = plt.subplots()
    while not p.percolates():
        p.open(np.random.randint(1, p._n+1), np.random.randint(1, p._n+1))

    for i in range(0, p._n):
        for j in range(0, p._n):
            ax.add_patch(plt.Rectangle((j, p._n - 1 - i), 1, 1, color=get_cell_color(i+1, j+1, p)))

    ax.set_xlim(0, p._n)  
    ax.set_ylim(0, p._n)  
    ax.set_aspect('equal')
    ax.axis('on') 
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.title(f"{p.number_of_open_sites()} open sites")
    plt.show()

# returns the color of the cell based on its state
def get_cell_color(row, col, p):   
    if p.is_full(row, col):
        return "blue"
    elif p.is_open(row, col):
        return "white"
    else:
        return "black"

def main():
    #demo of the percolation class
    p = Percolation(20)
    draw_grid(p)

if __name__ == "__main__":
    main()
