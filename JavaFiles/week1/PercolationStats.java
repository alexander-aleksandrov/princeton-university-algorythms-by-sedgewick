package week1;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private double[] trialsResults;

    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("n and trials must be greater than 0");
        }
        trialsResults = new double[trials];
        for (int i = 0; i < trials; i++) {
            Percolation perc = new Percolation(n);
            while (!perc.percolates()) {
                int row = StdRandom.uniform(1, n + 1);
                int col = StdRandom.uniform(1, n + 1);
                perc.open(row, col);
            }
            trialsResults[i] = (double) perc.numberOfOpenSites() / (n * n);
        }
    }

    public double mean() {
        return StdStats.mean(trialsResults);
    }

    public double stddev() {
        return StdStats.stddev(trialsResults);
    }

    public double confidenceLo() {
        return mean() - 1.96 * stddev() / Math.sqrt(trialsResults.length);
    }

    public double confidenceHi() {
        return mean() + 1.96 * stddev() / Math.sqrt(trialsResults.length);
    }

    
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats stats = new PercolationStats(n, trials);

        System.out.println("Mean: " + stats.mean());
        System.out.println("Standard deviation: " + stats.stddev());
        System.out.println("95% confidence interval: [" + stats.confidenceLo() + ", " + stats.confidenceHi() + "]");
    }
}
