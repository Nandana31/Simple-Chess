import chess
import chess.svg

def minmax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_of(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            max_eval = max(max_eval, eval)
            board.pop()
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minmax(board, depth - 1, True)
            min_eval = min(min_eval, eval)
            board.pop()
        return min_eval

def evaluate_of(board):
    
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        if piece.color == chess.WHITE:
            score += piece_value_of(piece)
        else:
            score -= piece_value_of(piece)
    return score

def piece_value_of(piece):
    if piece is None:
        return 0
    piece_type = piece.piece_type
    if piece_type == chess.PAWN:
        return 1
    elif piece_type == chess.KNIGHT:
        return 3
    elif piece_type == chess.BISHOP:
        return 3
    elif piece_type == chess.ROOK:
        return 5
    elif piece_type == chess.QUEEN:
        return 9
    elif piece_type == chess.KING:
        return 0  
def get_the_best_move_of(board, depth):
    best_move = None
    max_eval = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        eval = minmax(board, depth - 1, False)
        if eval > max_eval:
            max_eval = eval
            best_move = move
        board.pop()
    return best_move

def play_chess_game():
    board = chess.Board()
    depth = 2  

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            print(board)
            move = input("Enter the move you wish to make: ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move. Try again!!!")
        else:
            print(board)
            print("AI model is thinking...")
            best_move = get_the_best_move_of(board, depth)
            board.push(best_move)

    print("Game over!!")
    result = board.result()
    if result == "1-0":
        print("The White wins!")
    elif result == "0-1":
        print("The Black wins!")
    else:
        print("Sorry!!!It's a draw!")

if __name__ == "__main__":
    play_chess_game()



