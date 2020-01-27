from agents import CommandLineAgent, DeepQLearningAgent, RandomAgent, RandomRolloutAgent
from environments.connect4 import Connect4GameState
from runners import run_to_the_end, run_for_n_games_and_print_stats, run_step, run_for_n_games_and_print_stats_1
import sys

if __name__ == "__main__":
    gs = Connect4GameState()
    agent1 = DeepQLearningAgent(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                                hidden_layers=5)
    agent0 = RandomRolloutAgent(50, False)
    agent1.alpha = 0.1
    agent1.epsilon = 0.6

    for i in range(int(sys.argv[2])):
        run_for_n_games_and_print_stats([agent0, agent1], gs, int(sys.argv[1]))

    agent1.epsilon = -1.0
    run_for_n_games_and_print_stats_1([agent0, agent1], gs, int(sys.argv[1]), "connect4_deepQlearning_" + sys.argv[1] + '_' + sys.argv[2])


