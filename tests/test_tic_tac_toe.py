import random

from pset0.tictactoe import TicTacToe, StudentAgent
from pset0.tictactoe_utils import AgentProtocol, Tile, Player, MoveStatus, GameStatus, RandomAgent


def test_tic_tac_toe():
    game = TicTacToe()
    assert game.board == [[Tile.EMPTY for _ in range(3)] for _ in range(3)]
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 0) == MoveStatus.SUCCESSFUL and game.board[0][0] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 0) == MoveStatus.CELL_TAKEN and game.board[0][0] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(1, 1) == MoveStatus.SUCCESSFUL and game.board[1][1] == "O"
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 1) == MoveStatus.SUCCESSFUL and game.board[0][1] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(2, 2) == MoveStatus.SUCCESSFUL and game.board[2][2] == "O"
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.IN_PROGRESS

    assert game.make_move(0, 2) == MoveStatus.SUCCESSFUL and game.board[0][2] == "X"
    assert game.current_player == Player.O
    assert game.game_status() == GameStatus.X

    assert game.make_move(1, 0) == MoveStatus.GAME_OVER
    assert game.current_player == Player.X
    assert game.game_status() == GameStatus.X


def game_loop(agent_x: AgentProtocol, agent_o: AgentProtocol) -> GameStatus:
    game = TicTacToe()
    while game.game_status() == GameStatus.IN_PROGRESS:
        if game.current_player == Player.X:
            row, col = agent_x.get_action(game)
        else:
            row, col = agent_o.get_action(game)
        game.make_move(row, col)

    return game.game_status()


def test_win_rate():
    wins = 0
    for _ in range(100):
        if random.random() < 0.5:
            agent_x = StudentAgent()
            agent_o = RandomAgent()
        else:
            agent_x = RandomAgent()
            agent_o = StudentAgent()

        result = game_loop(agent_x, agent_o)
        if result == GameStatus.X and isinstance(agent_x, StudentAgent):
            wins += 1
        elif result == GameStatus.O and isinstance(agent_o, StudentAgent):
            wins += 1

    assert wins >= 75
