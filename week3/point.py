class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Замените на соответствующий вызов в вашей графической библиотеке
        pass

    def drawTo(self, that):
        # Замените на соответствующий вызов в вашей графической библиотеке
        pass

    def slopeTo(self, that):
        if self.x == that.x and self.y == that.y:
            return float('-inf')  # Совпадающие точки
        elif self.x == that.x:
            return float('inf')  # Вертикальная линия
        elif self.y == that.y:
            return 0.0  # Горизонтальная линия
        else:
            return (that.y - self.y) / (that.x - self.x)
    
    def compareTo(self, that):
        if self.y < that.y or (self.y == that.y and self.x < that.x):
            return -1
        elif self.y > that.y or (self.y == that.y and self.x > that.x):
            return 1
        else:
            return 0

    def __lt__(self, that):
        return (self.y, self.x) < (that.y, that.x)

    def __eq__(self, that):
        return self.x == that.x and self.y == that.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def slope_order():
        def comparator(p1, p2):
            return cmp(self.slopeTo(p1), self.slopeTo(p2))
        return comparator

# Пример использования
if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    print(p1, "to", p2, "slope:", p1.slopeTo(p2))
