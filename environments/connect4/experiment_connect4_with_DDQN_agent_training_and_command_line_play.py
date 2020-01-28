from agents import DDQNAgent, RandomAgent
from environments.connect4 import Connect4GameState
from runners import run_for_n_games_and_print_stats_1, run_step

if __name__ == "__main__":
    gs = Connect4GameState()
    agent0 = DDQNAgent(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                                hidden_layers=5)
    agent0.alpha = 0.1
    agent0.epsilon = 0.005
    agent1 = RandomAgent()

    # for i in range(100):
    #     run_for_n_games_and_print_stats([agent0, agent1], gs, 5000)

    run_for_n_games_and_print_stats_1([agent0, agent1], gs, 10000, "C4_DDQN_10000")

