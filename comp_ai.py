import random


def ai_play(user_move, comp_move):
    possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for move, ai_move, player_move in zip(possible_choices, comp_move, user_move):
        while int(move) == int(player_move) or int(move) == int(ai_move):
            possible_choices.pop(move)
            choice_list = possible_choices
            return str(random.choice(choice_list))
    return str(random.choice(possible_choices))
