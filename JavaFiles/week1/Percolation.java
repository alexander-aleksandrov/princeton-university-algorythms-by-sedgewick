package week1;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private final int n;
    private final WeightedQuickUnionUF qu;
    private boolean[] grid;
    private int count;

    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("n must be greater than 0");
        }
        this.n = n;
        this.qu = new WeightedQuickUnionUF(n * n + 2);
        this.grid = new boolean[n * n];
        this.count = 0;
    }

    private int id(int row, int col) {
        return (row - 1) * n + (col - 1);
    }

    public void open(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Invalid row or column");
        }
        if (!isOpen(row, col)) {
            grid[id(row, col)] = true;
            count++;
            checkNeighbours(row, col);
        }
    }

    private void checkNeighbours(int row, int col) {
        int index = id(row, col);
        if (row == 1) {
            qu.union(index, 0);
        }
        if (row == n) {
            qu.union(index, n * n + 1);
        }
        if (row > 1 && isOpen(row - 1, col)) {
            qu.union(index, id(row - 1, col));
        }
        if (row < n && isOpen(row + 1, col)) {
            qu.union(index, id(row + 1, col));
        }
        if (col > 1 && isOpen(row, col - 1)) {
            qu.union(index, id(row, col - 1));
        }
        if (col < n && isOpen(row, col + 1)) {
            qu.union(index, id(row, col + 1));
        }
    }

    public boolean isOpen(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Invalid row or column");
        }
        return grid[id(row, col)];
    }

    public boolean isFull(int row, int col) {
        if (row < 1 || row > n || col < 1 || col > n) {
            throw new IllegalArgumentException("Invalid row or column");
        }
        return isOpen(row, col) && qu.connected(0, id(row, col));
    }

    public int numberOfOpenSites() {
        return count;
    }

    public boolean percolates() {
        return qu.connected(0, n * n + 1);
    }
}
