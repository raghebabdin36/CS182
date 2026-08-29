import random

from pset0.tic_tac_toe import TicTacToe, StudentAgent
from pset0.tic_tac_toe_utils import AgentProtocol, Player, MoveStatus, GameStatus, RandomAgent


def game_loop(agent_x: AgentProtocol, agent_o: AgentProtocol) -> GameStatus:
    game = TicTacToe()
    while game.game_status() == GameStatus.IN_PROGRESS:
        if game.current_player == Player.X:
            row, col = agent_x.get_action(game)
        else:
            row, col = agent_o.get_action(game)
        move_status = game.make_move(row, col)
        assert move_status == MoveStatus.SUCCESS

    return game.game_status()


def test_extra_credit():
    wins = 0
    for _ in range(100):
        if random.random() < 0.5:
            agent_x = StudentAgent()
            agent_o = RandomAgent()
        else:
            agent_x = RandomAgent()
            agent_o = StudentAgent()

        result = game_loop(agent_x, agent_o)
        if (
            result == GameStatus.X_WINS and isinstance(agent_x, StudentAgent)
            or result == GameStatus.O_WINS and isinstance(agent_o, StudentAgent)
        ):
            wins += 1

    assert wins >= 75
