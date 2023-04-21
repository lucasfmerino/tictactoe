from mod_ttt import *

x = []
o = []
win_con = False
player = "X"
print_board(x, o)

while not win_con:
    print(f"Player {player}, it's your turn.")
    play = input("Enter a number from 1-9: ")

    try:
        play = int(play)
    except ValueError:
        print("Invalid input! Please enter a number from 1-9.")
        print()
        continue

    if not is_valid_play(play, x, o):
        print("Invalid play! Please choose a free position on the board.")
        print()
        continue

    # Adicionar jogada do jogador atual na lista correspondente (X ou O)
    if player == "X":
        x.append(play)
    else:
        o.append(play)

    print_board(x, o)

    # Verificar se o jogador atual venceu ou houve empate
    if any(set(win) <= set(x) for win in WINNING_COMBOS) or any(set(win) <= set(o) for win in WINNING_COMBOS):
        print(f"Congratulations player {player}! You won the game.")
        win_con = True
    elif len(x) + len(o) == 9:
        print("It's a draw!")
        win_con = True

    # Trocar o jogador atual
    player = switch_player(player)
