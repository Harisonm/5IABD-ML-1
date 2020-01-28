from agents import DDQNAgentWithPER, RandomAgent, DDQNAgentWithER, DDQNAgent, \
    DeepQLearningAgent, PPOAgent, \
    ReinforceAgent, ReinforceMeanBaselineAgent, \
    tabular_like_deep_q_learning_agent, tabular_q_learning_agent, RandomRolloutAgent
from environments.connect4 import Connect4GameState
from runners import run_for_n_games_and_print_stats_1, run_step

if __name__ == "__main__":
    gs = Connect4GameState()
    agent0 = DDQNAgentWithPER(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                                hidden_layers=5)
    agent0.alpha = 0.1
    agent0.epsilon = 0.005

    agent1 = RandomAgent()

    agent2 = DDQNAgentWithER(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                              hidden_layers=5)
    agent2.alpha = 0.1
    agent2.epsilon = 0.005

    agent3 = DDQNAgent(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                              hidden_layers=5)
    agent3.alpha = 0.1
    agent3.epsilon = 0.005

    agent4 = DeepQLearningAgent(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                       hidden_layers=5)
    agent4.alpha = 0.1
    agent4.epsilon = 0.005

    agent5 = PPOAgent(
        state_space_size=gs.get_vectorized_state().shape[0],
        action_space_size=gs.get_action_space_size())

    agent6 = RandomRolloutAgent(100, False)

    agent7 = ReinforceAgent(
        state_space_size=gs.get_vectorized_state().shape[0],
        action_space_size=gs.get_action_space_size())

    agent9 = ReinforceMeanBaselineAgent(
        state_space_size=gs.get_vectorized_state().shape[0],
        action_space_size=gs.get_action_space_size())

    




    # for i in range(100):
    #     run_for_n_games_and_print_stats([agent0, agent1], gs, 5000)

    run_for_n_games_and_print_stats_1([agent0, agent1], gs, 10000, "C4_DDQNAgentWithPER_10000")

