import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdOut;

public class Solver {

    private boolean isSolvable;

    private int moves;

    private SearchBoard solutionBoard;

    private class SearchBoard implements Comparable<SearchBoard>
    {
        private Board board;

        private SearchBoard previousBoard;

        private int moves;

        private int priority;

        public SearchBoard(Board board, int moves, SearchBoard previousBoard) {
            this.board = board;
            this.moves = moves;
            this.previousBoard = previousBoard;

            priority = board.manhattan() + this.moves;
        }

        public int compareTo(SearchBoard that) {
            if (this.priority > that.priority) {
                return 1;
            }

            if (this.priority < that.priority) {
                return -1;
            }

            return 0;
        }
    }

    public Solver(Board initial)
    {
        MinPQ<SearchBoard> searchBoardQueue = new MinPQ<>();
        MinPQ<SearchBoard> searchTwinBoardQueue = new MinPQ<>();

        searchBoardQueue.insert(new SearchBoard(initial, 0, null));
        searchTwinBoardQueue.insert(new SearchBoard(initial.twin(), 0, null));

        while (true) {
            SearchBoard minBoard = searchBoardQueue.delMin();
            SearchBoard minTwinBoard = searchTwinBoardQueue.delMin();

            if (minBoard.board.isGoal()) {
                solutionBoard = minBoard;
                isSolvable = true;
                moves = minBoard.moves;
                break;
            }

            if (minTwinBoard.board.isGoal()) {
                isSolvable = false;
                moves = -1;
                break;
            }

            enqueueNeighbors(minBoard, searchBoardQueue);
            enqueueNeighbors(minTwinBoard, searchTwinBoardQueue);
        }
    }

    public boolean isSolvable()
    {
        return isSolvable;
    }

    public int moves()
    {
        return moves;
    }

    public Iterable<Board> solution()
    {
        if (!isSolvable) {
            return null;
        }

        Stack<Board> solution = new Stack<>();
        SearchBoard board = solutionBoard;
        while (board != null) {
            solution.push(board.board);
            board = board.previousBoard;
        }

        return solution;
    }

    private void enqueueNeighbors(SearchBoard searchBoard, MinPQ<SearchBoard> queue)
    {
        for (Board nextBoard: searchBoard.board.neighbors()) {
            if ((searchBoard.previousBoard == null) || (!nextBoard.equals(searchBoard.previousBoard.board))) {
                queue.insert(new SearchBoard(nextBoard, searchBoard.moves + 1, searchBoard));
            }
        }
    }

    public static void main(String[] args) {
        // create initial board from file
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] tiles = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                tiles[i][j] = in.readInt();
        Board initial = new Board(tiles);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}
