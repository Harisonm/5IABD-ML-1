from agents import CommandLineAgent, DeepQLearningAgent, RandomRolloutAgent
from environments.battleship import BattleshipGameState
from runners import run_to_the_end, run_for_n_games_and_print_stats,run_step

if __name__ == "__main__":
    gs = BattleshipGameState()
    gs.put_all_boat()

    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')
    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')

    agent0 = DeepQLearningAgent(action_space_size=gs.get_action_space_size(),
                                neurons_per_hidden_layer=128,
                                hidden_layers=5)
    agent1 = RandomRolloutAgent(100, False)

    agent0.alpha = 0.1
    agent0.epsilon = 0.3

    for i in range(100):
        run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

    agent0.epsilon = -1.0
    run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

    gs_clone = gs.clone()
    while not gs_clone.is_game_over():
        run_step([agent0, CommandLineAgent()], gs_clone)
        print(gs_clone)

    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')
    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')
