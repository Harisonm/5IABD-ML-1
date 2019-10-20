from agents import CommandLineAgent, RandomRolloutAgent
from environments.battleship import BattleshipGameState
from runners import run_to_the_end, run_for_n_games_and_print_stats

if __name__ == "__main__":
    gs = BattleshipGameState()
    gs.put_all_boat()

    agent0 = RandomRolloutAgent(10, False)
    agent1 = RandomRolloutAgent(10, False)

    run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

