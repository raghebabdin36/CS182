from __future__ import annotations

import random
import itertools

from enum import StrEnum
from typing import Protocol, runtime_checkable, TYPE_CHECKING

if TYPE_CHECKING:
    from pset0.tictactoe import TicTacToe


@runtime_checkable
class AgentProtocol(Protocol):
    def get_action(self, game: TicTacToe) -> tuple[int, int]: ...


class Player(StrEnum):
    X = "X"
    O = "O"

    def other(self) -> Player:
        return Player.O if self == Player.X else Player.X


class Tile(StrEnum):
    X = "X"
    O = "O"
    EMPTY = " "


class MoveStatus(StrEnum):
    SUCCESSFUL = "Move successful"
    OUT_OF_BOUNDS = "Invalid move: Out of bounds"
    CELL_TAKEN = "Invalid move: Cell already taken"
    GAME_OVER = "Invalid move: Game is already over"


class GameStatus(StrEnum):
    IN_PROGRESS = "In Progress"
    X = "X wins"
    O = "O wins"
    DRAW = "Draw"


class RandomAgent:
    def get_action(self, game: TicTacToe) -> tuple[int, int]:
        """
        Chooses a random valid move on the current board.
        """
        available_moves = [
            move for move in itertools.product(range(3), range(3)) if game.board[move[0]][move[1]] == Tile.EMPTY
        ]

        return random.choice(available_moves)
