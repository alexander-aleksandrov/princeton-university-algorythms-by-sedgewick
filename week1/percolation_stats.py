import numpy as np
from percolation import Percolation

class PercolationStats:
    def __init__(self, n, trials):
        # Perform independent trials on an n-by-n grid
        self.trials_results = []
        for _ in range(trials):
            p = Percolation(n) 
            while not p.percolates():
                p.open(np.random.randint(1, p._n+1), np.random.randint(1, p._n+1))
            self.trials_results.append(p.count / (n * n))

    def mean(self):
        # Sample mean of percolation threshold
        return np.mean(self.trials_results)

    def stddev(self):
        # Sample standard deviation of percolation threshold
        return np.std(self.trials_results)

    def confidenceLo(self):
        # Low endpoint of 95% confidence interval
        return self.mean() - 1.96 * self.stddev() / np.sqrt(len(self.trials_results))

    def confidenceHi(self):
        # High endpoint of 95% confidence interval
        return self.mean() + 1.96 * self.stddev() / np.sqrt(len(self.trials_results))

# Test client
if __name__ == "__main__":

    stats = PercolationStats(200, 100)
    
    print("Mean: ", stats.mean())
    print("Standard deviation: ", stats.stddev())
    print("95% confidence interval: [", stats.confidenceLo(), ",", stats.confidenceHi(), "]")
