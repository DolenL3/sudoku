class Grid:
    def __init__(self, n=3):
        self.n = n
        self.table = [[0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9]
        for row in range (9):
            for column in range (9):
                self.table[row][column]=int(((row*n + row/n + column) % (n*n) + 1))

    def __del__(self):
        pass

    def draw(self):
        for i in range (9):
            print (self.table[i])
table = Grid()
table.draw()
