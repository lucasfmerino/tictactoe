def switch_player(player):
    """
    Função para trocar o jogador atual (X ou O)
    """
    return "X" if player == "O" else "O"


def get_symbol(position, x, o):
    """
    Função para obter o símbolo do jogador em uma posição do tabuleiro
    """
    if position in x:
        return "X"
    elif position in o:
        return "O"
    else:
        return " "


def is_valid_play(play, x, o):
    """
    Função para verificar se a jogada é válida (posição livre no tabuleiro)
    """
    return 1 <= play <= 9 and play not in x and play not in o


def print_board(x, o):
    """
    Função para imprimir o tabuleiro com as jogadas atualizadas
    """
    board = f'''
 {get_symbol(7, x, o)} | {get_symbol(8, x, o)} | {get_symbol(9, x, o)} 
---+---+---
 {get_symbol(4, x, o)} | {get_symbol(5, x, o)} | {get_symbol(6, x, o)} 
---+---+---
 {get_symbol(1, x, o)} | {get_symbol(2, x, o)} | {get_symbol(3, x, o)} 
'''
    print(board)


WINNING_COMBOS = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
