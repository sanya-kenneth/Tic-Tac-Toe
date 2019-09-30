from board import Board, grid_spaces
from utilities import display_players, validate_gameplay
from comp_ai import ai_play

player_moves = []
comp_moves = []
game_board = Board()

print("\n Welcome to Sanya's Tic Tac Toe game")
print(game_board.display_board())
player = input("Please select [x] or [o]  to pick your player\n")
while player != 'x' and player != 'o':
    player = input(
        "\n Invalid player entry! Please select [x] or [o]  to pick your player\n \n")
    if player == 'x' or player == 'o':
        break
player = display_players(player)['user']
ai_player = display_players(player)['comp']
print(
    f"\n You have chosen player {player} and the computer is {ai_player} \n")

while True:
    user_choice = validate_gameplay(
        input("Please Select a number from [1] to [9]"))
    # print(player_moves)
    # print(comp_moves)
    if user_choice not in player_moves and user_choice not in comp_moves:
        game_board.update_board(user_choice, player)
        player_moves.append(user_choice)
        game_board.clear_board()
        print(game_board.display_board())
    ai_choice = ai_play(player_moves, comp_moves)
    print(ai_choice)
    # if ai_choice not in player_moves and ai_choice not in comp_moves:
    # ai_choice = ai_play()
    game_board.update_board(ai_choice, ai_player)
    comp_moves.append(ai_play(player_moves, comp_moves))
    game_board.clear_board()
    print(game_board.display_board())
