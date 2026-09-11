from pset0.tic_tac_toe_utils import GameStatus, MoveStatus, Player, Tile


class TicTacToe:
    def __init__(self):
        """
        Initializes an empty Tic-Tac-Toe board as a two-dimensional list,
        and sets the current player to 'X'.
        """
        self._board: list[list[Tile]] = [[Tile.EMPTY for _ in range(3)] for _ in range(3)]
        self._current_player: Player = Player.X

    @property
    def board(self) -> list[list[Tile]]:
        """
        Returns the current state of the board.
        """
        return self._board

    @property
    def current_player(self) -> Player:
        """
        Returns the current player.
        """
        return self._current_player

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
        if self.game_status() != GameStatus.IN_PROGRESS:
            return MoveStatus.GAME_OVER

        if row < 0 or row > 2 or col < 0 or col > 2:
            return MoveStatus.OUT_OF_BOUNDS

        if self._board[row][col] != Tile.EMPTY:
            return MoveStatus.CELL_TAKEN

        self._board[row][col] = Tile.X if self._current_player == Player.X else Tile.O
        self._current_player = self._current_player.other()
        return MoveStatus.SUCCESS

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
        lines = []
        for i in range(3):
            lines.append([self._board[i][0], self._board[i][1], self._board[i][2]])
            lines.append([self._board[0][i], self._board[1][i], self._board[2][i]])
        lines.append([self._board[0][0], self._board[1][1], self._board[2][2]])
        lines.append([self._board[0][2], self._board[1][1], self._board[2][0]])

        for line in lines:
            if line[0] != Tile.EMPTY and line[0] == line[1] == line[2]:
                return GameStatus.X_WINS if line[0] == Tile.X else GameStatus.O_WINS

        for row in self._board:
            for tile in row:
                if tile == Tile.EMPTY:
                    return GameStatus.IN_PROGRESS

        return GameStatus.DRAW


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
        me = Tile.X if game.current_player == Player.X else Tile.O
        opponent = Tile.O if me == Tile.X else Tile.X
        empty = [(r, c) for r in range(3) for c in range(3) if game.board[r][c] == Tile.EMPTY]

        for move in empty:
            if self._would_win(game.board, move, me):
                return move

        for move in empty:
            if self._would_win(game.board, move, opponent):
                return move

        for preferred in [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1)]:
            if preferred in empty:
                return preferred

        return empty[0]

    def _would_win(self, board: list[list[Tile]], move: tuple[int, int], tile: Tile) -> bool:
        row, col = move
        board[row][col] = tile
        won = self._has_three_in_a_row(board, tile)
        board[row][col] = Tile.EMPTY
        return won

    def _has_three_in_a_row(self, board: list[list[Tile]], tile: Tile) -> bool:
        lines = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]
        return any(line == [tile, tile, tile] for line in lines)
