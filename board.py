class Board:
    def __init__(self, board, WIDTH):
        self.field = board[:]
        self.WIDTH = WIDTH

    def update(self):
        a = self.field
        field = [[0] * self.WIDTH for i in range(self.WIDTH)]
        for i in range(self.WIDTH):
            for j in range(self.WIDTH):
                if i == 0 and j == 0:
                    n = a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
                elif i == 0 and j == self.WIDTH - 1:
                    n = a[i][j - 1] + a[i + 1][j] + a[i + 1][j - 1]
                elif i == self.WIDTH - 1 and j == 0:
                    n = a[i][j + 1] + a[i - 1][j] + a[i - 1][j + 1]
                elif i == self.WIDTH - 1 and j == self.WIDTH - 1:
                    n = a[i - 1][j] + a[i][j - 1] + a[i - 1][j - 1]
                elif i == 0:
                    n = a[i][j - 1] + a[i][j + 1] + sum(a[i + 1][j - 1:j + 2])
                elif i == self.WIDTH - 1:
                    n = a[i][j - 1] + a[i][j + 1] + sum(a[i - 1][j - 1:j + 2])
                elif j == 0:
                    n = a[i - 1][j] + a[i + 1][j] + a[i - 1][j + 1] + a[i][j + 1] + a[i + 1][j + 1]
                elif j == self.WIDTH - 1:
                    n = a[i - 1][j] + a[i + 1][j] + a[i - 1][j - 1] + a[i][j - 1] + a[i + 1][j - 1]
                else:
                    n = sum(a[i - 1][j - 1:j + 2]) + sum(a[i][j - 1:j + 2]) + sum(a[i + 1][j - 1:j + 2]) - a[i][j]
                if n == 3:
                    field[i][j] = 1
                elif n == 2 and a[i][j] == 1:
                    field[i][j] = 1
        self.field = field

    def __str__(self):
        res = ''
        for i in range(self.WIDTH):
            res = res + ' '.join([str(x) for x in self.field[i]]) + '\n'
        return res

