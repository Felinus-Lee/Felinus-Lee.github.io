# 定义棋盘大小
BOARD_SIZE = 15

# 定义棋子类型的枚举
class Piece:
    EMPTY = 0
    BLACK = 1
    WHITE = 2

# 棋盘类
class Board:
    def __init__(self):
        self.board = [[Piece.EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    
    def is_valid_move(self, row, col):
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and self.board[row][col] == Piece.EMPTY
    
    def make_move(self, row, col, piece):
        self.board[row][col] = piece
    
    def undo_move(self, row, col):
        self.board[row][col] = Piece.EMPTY
    
    def is_game_over(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] != Piece.EMPTY:
                    if self.check_five(row, col):
                        return True
        return False
    
    def check_five(self, row, col):
        piece = self.board[row][col]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 水平、垂直、主对角线、副对角线
        for dr, dc in directions:
            count = 1  # 当前位置已经有一个棋子
            r, c = row, col
            while True:
                r += dr
                c += dc
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == piece:
                    count += 1
                else:
                    break
            r, c = row, col
            while True:
                r -= dr
                c -= dc
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and self.board[r][c] == piece:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False