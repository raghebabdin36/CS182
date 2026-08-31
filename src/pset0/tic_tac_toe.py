from pset0.tic_tac_toe_utils import GameStatus, MoveStatus, Player, Tile


class TicTacToe:
    def __init__(self):
        """
        Initializes an empty Tic-Tac-Toe board as a two-dimensional list,
        and sets the current player to 'X'.
        """
        raise NotImplementedError

    @property
    def board(self) -> list[list[Tile]]:
        """
        Returns the current state of the board.
        """
        raise NotImplementedError

    @property
    def current_player(self) -> Player:
        """
        Returns the current player.
        """
        raise NotImplementedError

    def make_move(self, row: int, col: int) -> MoveStatus:
        """
        Updates the board if the move is valid. A move is invalid if the tile
        specified is already taken, or the tile is out of bounds (i.e., the
        row or column index are not between 0 and 2 inclusive). If the move is
        successful, the current player is set to the opposite player.

        Parameters:
            `row`: The desired row index (0, 1, or 2).
            `col`: The desired column index (0, 1, or 2).

        Returns:
            The result of the move attempt, which can be one of the following:
            - MoveStatus.SUCCESS: The move was successful.
            - MoveStatus.OUT_OF_BOUNDS: The specified cell is out of bounds.
            - MoveStatus.CELL_TAKEN: The specified cell is already taken.
            - MoveStatus.GAME_OVER: The game is no longer in progress.
        """
        raise NotImplementedError

    def game_status(self) -> GameStatus:
        """
        Gets the current status of the game.

        Returns:
            The current status of the game, which can be one of the following:
            - GameStatus.X_WINS: Player X has won the game.
            - GameStatus.O_WINS: Player O has won the game.
            - GameStatus.DRAW: The game is a draw.
            - GameStatus.IN_PROGRESS: The game is still in progress.
        """
        raise NotImplementedError


class StudentAgent:
    def __init__(self):
        pass

    def get_action(self, game: TicTacToe) -> tuple[int, int]:
        """
        Chooses a move based on an algorithm of your choice. For extra credit,
        your agent should win at least 75% of games against a random agent,
        regardless of which player it takes.

        Parameters:
            `game`: An instance of Tic-Tac-Toe.

        Returns:
            A (row, col) pair, representing a move.
        """
        raise NotImplementedError
