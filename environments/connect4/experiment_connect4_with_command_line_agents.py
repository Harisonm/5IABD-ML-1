from agents import CommandLineAgent
from environments.connect4.connect_4 import Connect4GameState
from runners import run_to_the_end

if __name__ == "__main__":
    gs = Connect4GameState()
    agent = CommandLineAgent()

    print(gs)
    run_to_the_end([agent, agent], gs)
    print(gs)
