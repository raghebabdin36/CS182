from pset0.tic_tac_toe import TicTacToe
from pset0.tic_tac_toe_utils import Tile, Player, MoveStatus, GameStatus


def test_tic_tac_toe():
    game = TicTacToe()
    assert game.board == [[Tile.EMPTY for _ in range(3)] for _ in range(3)]
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 0) == MoveStatus.SUCCESS and game.board[0][0] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 0) == MoveStatus.CELL_TAKEN and game.board[0][0] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(1, 1) == MoveStatus.SUCCESS and game.board[1][1] == "O"
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 1) == MoveStatus.SUCCESS and game.board[0][1] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(2, 2) == MoveStatus.SUCCESS and game.board[2][2] == "O"
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 2) == MoveStatus.SUCCESS and game.board[0][2] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.X_WINS

    assert game.make_move(1, 0) == MoveStatus.GAME_OVER
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.X_WINS
