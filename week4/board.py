class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.n = len(tiles)

    def __str__(self):
        return str(self.n, "\n") + '\n'.join([' '.join(map(str, row)) for row in self.tiles])

    def dimension(self):
        return self.n

    def hamming(self):
        hamming_distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] != i * self.n + j + 1 and self.tiles[i][j] != 0:
                    hamming_distance += 1
        return hamming_distance

    def manhattan(self):
        manhattan_distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] != 0:
                    target_row, target_col = divmod(self.tiles[i][j] - 1, self.n)
                    manhattan_distance += abs(target_row - i) + abs(target_col - j)
        return manhattan_distance

    def is_goal(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] != 0 and self.tiles[i][j] != i * self.n + j + 1:
                    return False
        return True

    def equals(self, y):
        if not isinstance(y, Board):
            return False
        return self.tiles == y.tiles

    def __eq__(self, y):
        return self.equals(y)
    
    def __hash__(self):
        return hash(tuple(map(tuple, self.tiles)))

    def neighbors(self):
        neighbors = []
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] == 0:
                    if i > 0:
                        neighbor = self.tiles.copy()
                        neighbor[i][j], neighbor[i - 1][j] = neighbor[i - 1][j], neighbor[i][j]
                        neighbors.append(Board(neighbor))
                    if i < self.n - 1:
                        neighbor = self.tiles.copy()
                        neighbor[i][j], neighbor[i + 1][j] = neighbor[i + 1][j], neighbor[i][j]
                        neighbors.append(Board(neighbor))
                    if j > 0:
                        neighbor = self.tiles.copy()
                        neighbor[i][j], neighbor[i][j - 1] = neighbor[i][j - 1], neighbor[i][j]
                        neighbors.append(Board(neighbor))
                    if j < self.n - 1:
                        neighbor = self.tiles.copy()
                        neighbor[i][j], neighbor[i][j + 1] = neighbor[i][j + 1], neighbor[i][j]
                        neighbors.append(Board(neighbor))
                    return neighbors

    def twin(self):
        """
        A board that is obtained by exchanging any pair of tiles
        """
        twin = self.tiles.copy()
        for i in range(self.n):
            for j in range(self.n - 1):
                if twin[i][j] != 0 and twin[i][j + 1] != 0:
                    twin[i][j], twin[i][j + 1] = twin[i][j + 1], twin[i][j]
                    return Board(twin)


def main():
    pass

if __name__ == "__main__":
    main()
# Example usage:
# tiles = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
# board = Board(tiles)
# print(board)
# print("Hamming:", board.hamming())
# print("Manhattan:", board.manhattan())
# print("Is goal:", board.is_goal())
