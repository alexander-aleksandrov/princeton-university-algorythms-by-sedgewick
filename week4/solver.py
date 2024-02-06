import sys
from board import Board
from queue import PriorityQueue

class Solver():
    def __init__(self, initial: Board):
        if not initial:
            raise ValueError("Initial board is None")
        self.initial = initial
        self._moves = 0
        self._solution = []
        self.pq = PriorityQueue()
        self.came_from = {}
        self.solve()

    def solve(self):
        self.pq.put((0, self.initial))
        self.came_from[self.initial] = None  # Начальная доска не имеет предшественника
        paths_costs = {self.initial: 0}

        while not self.pq.empty():
            current_priority, current_board = self.pq.get()
            current_cost = paths_costs[current_board]

            if current_board.is_goal():
                self._moves = current_cost
                self._reconstruct_path(current_board)
                return

            for neighbor in current_board.neighbors():
                next_cost = current_cost + 1
                if neighbor not in paths_costs or next_cost < paths_costs[neighbor]:
                    paths_costs[neighbor] = next_cost
                    priority = next_cost + neighbor.manhattan()
                    self.pq.put((priority, neighbor))
                    self.came_from[neighbor] = current_board

    def _reconstruct_path(self, current_board):
        # Восстановление пути от конечной доски до начальной
        path = []
        while current_board:
            path.append(current_board)
            current_board = self.came_from[current_board]
        self._solution = path[::-1]  # Переворачиваем путь, чтобы начать с начальной доски

          


    def is_solvable(self):
        n = self.initial.dimension()
        tiles = self.initial.tiles
        inversions = 0
        for i in range(n * n - 1):
            for j in range(i + 1, n * n):
                if tiles[i // n][i % n] != 0 and tiles[j // n][j % n] != 0 and tiles[i // n][i % n] > tiles[j // n][j % n]:
                    inversions += 1
        if n % 2 == 0:
            inversions += self.initial.tiles[-1][-1] // n + self.initial.tiles[-1][-1] % n
        return inversions % 2 == 0

    def moves(self):
        if not self.is_solvable():
            return -1
        return self._moves
        

    def solution(self):
        if not self.is_solvable():
            return None
        return self._solution

def main():
    tiles = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]

    initial = Board(tiles)
    solver = Solver(initial)

    if not solver.is_solvable():
        print("No solution possible")
    else:
        print("Minimum number of moves =", solver.moves())
        for board in solver.solution():
            print(board)

if __name__ == "__main__":
    main()