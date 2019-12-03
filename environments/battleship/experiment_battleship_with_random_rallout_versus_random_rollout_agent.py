from agents import RandomRolloutAgent
from environments.battleship import BattleshipGameState
from runners import run_to_the_end, run_for_n_games_and_print_stats

if __name__ == "__main__":
    gs = BattleshipGameState()
    gs.put_all_boat()
    agent0 = RandomRolloutAgent(100, False)
    agent1 = RandomRolloutAgent(100, False)

    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')
    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')
    
    run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')
    print(gs.board_j0, '\n')
    print(gs.board_attack_j0, '\n')