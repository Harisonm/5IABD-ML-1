from agents import RandomRolloutAgent, RandomAgent
from environments.connect4 import Connect4GameState
from runners import run_to_the_end, run_for_n_games_and_print_stats_1
import sys

if __name__ == "__main__":
    gs = Connect4GameState()
    agent0 = RandomAgent()
    agent1 = RandomRolloutAgent(int(sys.argv[2]), False)

    run_for_n_games_and_print_stats_1([agent0, agent1], gs, int(sys.argv[1]), "connect4_" + sys.argv[1] + '_' + sys.argv[2])
