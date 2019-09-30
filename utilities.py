def display_players(player):
    """
    Display the user's player on the board
    """
    if player == 'x':
        user = 'x'
        ai_player = 'o'
    else:
        user = 'o'
        ai_player = 'x'
    return {'user': user, 'comp': ai_player}


def validate_gameplay(choice):
    """
    Checks and validates the user's choice while playing the game
    """
    accepted_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while choice not in accepted_choices:
        choice = input("\n Invalid Entry! Please enter a valid number\n")
        if choice in accepted_choices:
            return choice
    return choice


def check_selected_spaces(new_move, player_moves, comp_moves):
    if new_move in player_moves:
        pass
