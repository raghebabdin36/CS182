from pset0.tictactoe_utils import Tile, Player, MoveStatus, GameStatus


class TicTacToe:
    def __init__(self):
        """
        Initializes an empty 3x3 Tic-Tac-Toe board and sets the current player to 'X'.
        """

        raise NotImplementedError

    @property
    def board(self) -> list[list[Tile]]:
        """
        Returns the current state of the board as a 3x3 list of lists.
        """

        raise NotImplementedError

    @property
    def current_player(self) -> Player:
        """
        Returns the current player ('X' or 'O').

        Returns:
            Player: The current player, which can be either Player.X or Player.O.
        """

        raise NotImplementedError

    def make_move(self, row: int, col: int) -> MoveStatus:
        """
        Updates the board if the move is valid. A move is invalid if the tile at (col, row) is already taken
        or if the row or column value are out of bounds (not between 0 and 2 inclusive).
        If the move is successful, updates the current player to the other player.

        Parameters:
            row (int): The row index (0, 1, or 2) where the player wants to place their mark.
            col (int): The column index (0, 1, or 2) where the player wants to place their mark.

        Returns:
            MoveStatus: The result of the move attempt, which can be one of the following:
                - MoveStatus.SUCCESS: The move was successful.
                - MoveStatus.OUT_OF_BOUNDS: The specified row or column is out of bounds.
                - MoveStatus.CELL_TAKEN: The specified cell is already taken.
                - MoveStatus.GAME_OVER: The game is already over (either a player has won or the board is full).
        """

        raise NotImplementedError

    def game_status(self) -> GameStatus:
        """
        Gets the current status of the game.

        Returns:
            GameStatus: The current status of the game, which can be one of the following:
                - GameStatus.X_WINS: Player 'X' has won the game.
                - GameStatus.O_WINS: Player 'O' has won the game.
                - GameStatus.DRAW: The game is a draw (the board is full and there is no winner).
                - GameStatus.IN_PROGRESS: The game is still in progress (there are empty cells and no winner yet).
        """

        raise NotImplementedError


class StudentAgent:
    def __init__(self): ...

    def get_action(self, game: TicTacToe) -> tuple[int, int]:
        """
        Chooses a move based on an algorithm of your choice.

        EXTRA CREDIT: Implement an algorithm that can win at least 75% of games against a random agent, regardless of whether it plays first or second.
        """

        raise NotImplementedError
