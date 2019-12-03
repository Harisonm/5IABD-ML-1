from agents import CommandLineAgent, RandomRolloutAgent
from environments.battleship import BattleshipGameState
from runners import run_to_the_end

if __name__ == "__main__":
    gs = BattleshipGameState()
    gs.put_all_boat()

    agent0 = CommandLineAgent()
    agent1 = RandomRolloutAgent(100, False)

    print(gs.board_j0)
    print(gs.board_attack_j0)
    print(gs.board_j1)
    print(gs.board_attack_j1)

    run_to_the_end([agent0, agent1], gs)

    print(gs.board_j0)
    print(gs.board_attack_j0)
    print(gs.board_j1)
    print(gs.board_attack_j1)
