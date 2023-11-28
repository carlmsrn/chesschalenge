
import chess

tabuleiro = chess.Board()

pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rookstable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

def avaliar_tabuleiro():
    if tabuleiro.is_checkmate():
        if tabuleiro.turn:
            return -9999
        else:
            return 9999
    if tabuleiro.is_stalemate():
        return 0
    if tabuleiro.is_insufficient_material():
        return 0

    wp = len(tabuleiro.pieces(chess.PAWN, chess.WHITE))
    bp = len(tabuleiro.pieces(chess.PAWN, chess.BLACK))
    wn = len(tabuleiro.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(tabuleiro.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(tabuleiro.pieces(chess.BISHOP, chess.WHITE))
    bb = len(tabuleiro.pieces(chess.BISHOP, chess.BLACK))
    wr = len(tabuleiro.pieces(chess.ROOK, chess.WHITE))
    br = len(tabuleiro.pieces(chess.ROOK, chess.BLACK))
    wq = len(tabuleiro.pieces(chess.QUEEN, chess.WHITE))
    bq = len(tabuleiro.pieces(chess.QUEEN, chess.BLACK))

    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
    pawnsq = sum([pawntable[i] for i in tabuleiro.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)] for i in tabuleiro.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in tabuleiro.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] for i in tabuleiro.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([bishopstable[i] for i in tabuleiro.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)] for i in tabuleiro.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in tabuleiro.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] for i in tabuleiro.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in tabuleiro.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)] for i in tabuleiro.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in tabuleiro.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)] for i in tabuleiro.pieces(chess.KING, chess.BLACK)])

    avaliacao = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq

    if tabuleiro.turn:
        return avaliacao
    else:
        return -avaliacao

def alphabeta(alpha, beta, profundidade):
    melhor_pontuacao = -9999
    if profundidade == 0:
        return quiesce(alpha, beta)
    for movimento in tabuleiro.legal_moves:
        tabuleiro.push(movimento)
        pontuacao = -alphabeta(-beta, -alpha, profundidade - 1)
        tabuleiro.pop()
        if pontuacao >= beta:
            return pontuacao
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
        if pontuacao > alpha:
            alpha = pontuacao
    return melhor_pontuacao

def quiesce(alpha, beta):
    stand_pat = avaliar_tabuleiro()
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat
    for movimento in tabuleiro.legal_moves:
        if tabuleiro.is_capture(movimento):
            tabuleiro.push(movimento)
            pontuacao = -quiesce(-beta, -alpha)
            tabuleiro.pop()
            if pontuacao >= beta:
                return beta
            if pontuacao > alpha:
                alpha = pontuacao
    return alpha

def escolher_movimento(profundidade, color):
    melhor_movimento = chess.Move.null()
    melhor_pontuacao = -9999
    alpha = -10000
    beta = 10000
    for movimento in tabuleiro.legal_moves:
        tabuleiro.push(movimento)
        pontuacao_tabuleiro = -alphabeta(-beta, -alpha, profundidade - 1)
        if pontuacao_tabuleiro > melhor_pontuacao:
            melhor_pontuacao = pontuacao_tabuleiro
            melhor_movimento = movimento
        if pontuacao_tabuleiro > alpha:
            alpha = pontuacao_tabuleiro
        tabuleiro.pop()

    #print(f"\n{tabuleiro} \n")

    for square in chess.SQUARES:
        moves = get_piece_moves(tabuleiro, square, color)
        if moves:
            piece_type = tabuleiro.piece_at(square).piece_type
            print(f"{chess.piece_name(piece_type)}: {', '.join(moves)}")

    print(f"\nJogada do Bot: {melhor_movimento.uci()}\n")
    return melhor_movimento

# Pergunta ao jogador se ele quer ser as peças brancas ou pretas -------------------------------------
cor_peca = input("Escolha as peças que deseja jogar (Branco ou Preto): ").lower()

def get_piece_moves(board, square, color):
    piece = board.piece_at(square)
    if piece is not None and piece.color == color:
        return [move.uci() for move in board.legal_moves if move.from_square == square]
    return []


# Loop principal do jogo
while not tabuleiro.is_game_over():
    
    print("--------------------------------------------")
    print(f"\n{tabuleiro} \n")
    
    print("Peças disponíveis:\n")
    for square in chess.SQUARES:
        moves = get_piece_moves(tabuleiro, square, chess.WHITE if tabuleiro.turn == chess.WHITE else chess.BLACK)
        if moves:
            piece_type = tabuleiro.piece_at(square).piece_type
            print(f"{chess.piece_name(piece_type)} em {chess.square_name(square)}: {', '.join(moves)}")

    if tabuleiro.turn == chess.WHITE:
        if cor_peca == 'branco':
            # Se o jogador escolheu as peças brancas, ele faz a jogada
            move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e2e4'): ")
            while not (len(move_uci) == 4 and move_uci[0].isalpha() and move_uci[1].isdigit() and move_uci[2].isalpha() and move_uci[3].isdigit()):
                print("Entrada inválida. Tente novamente.")
                move_uci = input("Faça sua jogada (em formato UCI, ex: 'e2e4'): ")

            move = chess.Move.from_uci(move_uci)
            while move not in tabuleiro.legal_moves:
                print("Movimento inválido. Tente novamente.")
                move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e2e4'): ")
                move = chess.Move.from_uci(move_uci)

            tabuleiro.push(move)
        else:
            # Se o jogador escolheu as peças pretas, o computador faz a jogada
            computer_move = escolher_movimento(3, chess.BLACK)
            tabuleiro.push(computer_move)
    else:
        # Peças pretas (jogador ou computador, dependendo da escolha do jogador)
        if cor_peca == 'preto':
            move_uci = input("Faça sua jogada (em formato UCI, ex: 'e7e5'): ")
            while not (len(move_uci) == 4 and move_uci[0].isalpha() and move_uci[1].isdigit() and move_uci[2].isalpha() and move_uci[3].isdigit()):
                print("Entrada inválida. Tente novamente.")
                move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e7e5'): ")

            move = chess.Move.from_uci(move_uci)
            while move not in tabuleiro.legal_moves:
                print("Movimento inválido. Tente novamente.")
                move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e7e5'): ")
                move = chess.Move.from_uci(move_uci)

            tabuleiro.push(move)
        else:
            computer_move = escolher_movimento(3, chess.WHITE)
            tabuleiro.push(computer_move)

# Exibe o resultado do jogo
print("Fim do jogo. Resultado:", tabuleiro.result())





