from agents import RandomRolloutAgent, RandomAgent
from environments.tictactoe import TicTacToeGameState
from runners import run_to_the_end, run_for_n_games_and_print_stats_1
import sys

if __name__ == "__main__":
    gs = TicTacToeGameState()
    agent0 = RandomAgent()
    agent1 = RandomRolloutAgent(100, False)

    run_for_n_games_and_print_stats_1([agent0, agent1], gs, int(sys.argv[1]), "tictactoe_" + sys.argv[1])
