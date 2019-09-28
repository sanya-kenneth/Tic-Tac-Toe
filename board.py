from prettytable import PrettyTable

# grid spaces for the tic tac toe board
grid_spaces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


class Board(object):
    """
    game board instance
    """

    def __init__(self):
        self.board = PrettyTable(header=False, padding_width=2)
        self.separation_line = "---"

    def display_board(self):
        """
        Display Tic tac toe game
        """
        self.board.add_row(grid_spaces[0:3])
        self.board.add_row(self.separation_line)
        self.board.add_row(grid_spaces[3:6])
        self.board.add_row(self.separation_line)
        self.board.add_row(grid_spaces[6:])
        return self.board

    def update_board(self, choice, player):
        """
        update tic tac toe board based on the user's input

        Args:
            choice => player's choice on the board
            player => player that is currently making the move
        """
        if int(choice) == 1:
            grid_spaces[0] = player
        elif int(choice) == 2:
            grid_spaces[1] = player
        elif int(choice) == 3:
            grid_spaces[2] = player
        elif int(choice) == 4:
            grid_spaces[3] = player
        elif int(choice) == 5:
            grid_spaces[4] = player
        elif int(choice) == 6:
            grid_spaces[5] = player
        elif int(choice) == 7:
            grid_spaces[6] = player
        elif int(choice) == 8:
            grid_spaces[7] = player
        elif int(choice) == 9:
            grid_spaces[8] = player
        print(f"\n Player {player} made a move \n")
