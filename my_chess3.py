import chess
import time

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

tabuleiro_cache = {}

def avaliar_tabuleiro():
    board_key = tabuleiro.fen()
    if board_key in tabuleiro_cache:
        return tabuleiro_cache[board_key]

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

    tabuleiro_cache[board_key] = avaliacao
    return avaliacao

transposition_table = {}

def alphabeta(alpha, beta, profundidade):
    board_key = tabuleiro.fen()
    if board_key in transposition_table:
        entry = transposition_table[board_key]
        if entry['depth'] >= profundidade:
            if entry['flag'] == 'exact':
                return entry['score']
            elif entry['flag'] == 'lowerbound':
                alpha = max(alpha, entry['score'])
            elif entry['flag'] == 'upperbound':
                beta = min(beta, entry['score'])
            if alpha >= beta:
                return entry['score']

    melhor_pontuacao = -9999
    if profundidade == 0:
        return quiesce(alpha, beta)
    for movimento in sorted(tabuleiro.legal_moves, key=heuristica_de_ordem):
        tabuleiro.push(movimento)
        pontuacao = -alphabeta(-beta, -alpha, profundidade - 1)
        tabuleiro.pop()

        # Atualizar a tabela de transposição
        if pontuacao >= beta:
            transposition_table[board_key] = {'depth': profundidade, 'flag': 'lowerbound', 'score': beta}
            return beta
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
        if pontuacao > alpha:
            alpha = pontuacao

    # Atualizar a tabela de transposição
    transposition_table[board_key] = {'depth': profundidade, 'flag': 'exact', 'score': melhor_pontuacao}
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

def heuristica_de_ordem(move):
    if tabuleiro.is_capture(move):
        return 1
    elif not tabuleiro.gives_check(move) and chess.square_distance(move.from_square, move.to_square) <= 2:
        return 0
    else:
        return -1


def escolher_movimento(profundidade):
    melhor_movimento = chess.Move.null()
    melhor_pontuacao = -9999
    alpha = -10000
    beta = 10000

    start_time = time.time()  # Grava o tempo inicial

    for movimento in sorted(tabuleiro.legal_moves, key=heuristica_de_ordem):
        tabuleiro.push(movimento)
        pontuacao_tabuleiro = -alphabeta(-beta, -alpha, profundidade - 1)
        if pontuacao_tabuleiro > melhor_pontuacao:
            melhor_pontuacao = pontuacao_tabuleiro
            melhor_movimento = movimento
        if pontuacao_tabuleiro > alpha:
            alpha = pontuacao_tabuleiro
        tabuleiro.pop()

    end_time = time.time()  # Grava o tempo final
    elapsed_time = end_time - start_time

    print(f"\nTempo de processamento: {elapsed_time:.3f} segundos")

    return melhor_movimento

# Pergunta ao jogador se ele quer ser as peças brancas ou pretas
cor_peca = input("Escolha as peças que deseja jogar (Branco ou Preto): ").lower()

def get_piece_moves(board, square):
    piece = board.piece_at(square)
    if piece is not None:
        return [move.uci() for move in board.legal_moves if move.from_square == square]
    return []

# Loop principal do jogo
while not tabuleiro.is_game_over():
    print("----------------------------------")
    print(f"\n{tabuleiro}\n")
    while True:
        escolher_profundidade = input("Defina a profundidade (1 a 4): ")

        if escolher_profundidade.isdigit():  # Verifica se a entrada é um número
            escolher_profundidade = int(escolher_profundidade)

            if 1 <= escolher_profundidade <= 4:
                break  # Sai do loop se o número estiver no intervalo desejado
            else:
                print("Por favor, insira um número entre 1 e 4.")
        else:
            print("Por favor, insira um número válido.")

        # Agora você pode usar a variável escolher_profundidade no restante do seu código.
        print(f"Profundidade escolhida: {escolher_profundidade}")
    

    for square in chess.SQUARES:
        moves = get_piece_moves(tabuleiro, square)
        if moves:
            piece_type = tabuleiro.piece_at(square).piece_type
            print(f"{chess.piece_name(piece_type)}: {', '.join(moves)}")

    

    if tabuleiro.turn == chess.WHITE:
        if cor_peca == 'branco':
            move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e2e4'): ")
            move = chess.Move.from_uci(move_uci)
            while move not in tabuleiro.legal_moves:
                print("Movimento inválido. Tente novamente.")
                move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e2e4'): ")
                move = chess.Move.from_uci(move_uci)
            tabuleiro.push(move)
        else:
            computer_move = escolher_movimento(escolher_profundidade)
            tabuleiro.push(computer_move)
            print(f"\nJogada do bot: {computer_move.uci()}")  # Exibe a jogada do bot
    else:
        # Peças pretas (jogador ou computador, dependendo da escolha do jogador)
        if cor_peca == 'preto':
            
            move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e7e5'): ")
            move = chess.Move.from_uci(move_uci)
            while move not in tabuleiro.legal_moves:
                print("Movimento inválido. Tente novamente.")
                move_uci = input("\nFaça sua jogada (em formato UCI, ex: 'e7e5'): ")
                move = chess.Move.from_uci(move_uci)
            tabuleiro.push(move)
        else:
            computer_move = escolher_movimento(escolher_profundidade)
            tabuleiro.push(computer_move)
            print(f"\nJogada do bot: {computer_move.uci()}")  # Exibe a jogada do bot

# Exibe o resultado do jogo
print("Fim do jogo. Resultado:", tabuleiro.result())

