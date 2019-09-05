from agents import RandomAgent
from environments import GridWorldGameState
from runners import run_to_the_end

if __name__ == "__main__":
    gs = GridWorldGameState()
    agent = CommandLineAgent()

    print(gs)
    run_to_the_end([agent], gs)
    print(gs)