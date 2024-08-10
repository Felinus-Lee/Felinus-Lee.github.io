# DFS搜索函数
def dfs(board, depth, max_depth, player):
    if depth == max_depth or board.is_game_over():
        return evaluate(board, player)

    best_score = float('-inf') if player == Piece.BLACK else float('inf')
    moves = generate_moves(board)
    
    for move in moves:
        row, col = move
        board.make_move(row, col, player)
        
        score = dfs(board, depth + 1, max_depth, Piece.WHITE if player == Piece.BLACK else Piece.BLACK)
        
        board.undo_move(row, col)
        
        if player == Piece.BLACK:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)