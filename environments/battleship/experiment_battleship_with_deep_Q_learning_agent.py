from agents import CommandLineAgent
from environments.battleship import BattleshipGameState
from runners import run_to_the_end

if __name__ == "__main__":
    gs = BattleshipGameState()
    agent = CommandLineAgent()

    print(gs)
    run_to_the_end([agent, agent], gs)
    print(gs)
