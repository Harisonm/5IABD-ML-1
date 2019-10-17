from agents import CommandLineAgent, DeepQLearningAgent
from environments.connect4 import Connect4GameState
from runners import run_to_the_end

if __name__ == "__main__":
    gs = Connect4GameState()
    agent0 = CommandLineAgent()
    agent1 = DeepQLearningAgent(action_space_size=gs.get_action_space_size())
    agent1.alpha = 0.1
    agent1.epsilon = 0.005

    print(gs)
    run_to_the_end([agent0, agent1], gs)
    print(gs)