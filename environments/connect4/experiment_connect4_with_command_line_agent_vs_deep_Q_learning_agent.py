from agents import CommandLineAgent, DeepQLearningAgent
from environments.connect4 import Connect4GameState
from runners import run_to_the_end, run_for_n_games_and_print_stats, run_step

if __name__ == "__main__":
    gs = Connect4GameState()
    agent0 = DeepQLearningAgent(action_space_size=gs.get_action_space_size())
    agent1 = DeepQLearningAgent(action_space_size=gs.get_action_space_size())
    agent0.alpha = 0.1
    agent0.epsilon = 0.005
    agent1.alpha = 0.1
    agent1.epsilon = 0.005

    for i in range(500):
        run_for_n_games_and_print_stats([agent0, agent1], gs, 500)

    agent0.epsilon = -1.0
    agent1.epsilon = -1.0
    run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

    gs_clone = gs.clone()
    while not gs_clone.is_game_over():
        run_step([agent0, CommandLineAgent()], gs_clone)
        print(gs_clone)
