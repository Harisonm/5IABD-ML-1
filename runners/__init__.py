import timeit
from typing import List
import numpy as np

from contracts import Agent, GameState


def run_step(agents: List[Agent], gs: GameState):
    assert (not gs.is_game_over())
    active_player_index = gs.get_active_player()

    old_scores = gs.get_scores().copy()
    action = agents[active_player_index].act(gs)
    gs.step(active_player_index, action)
    new_scores = gs.get_scores()
    rewards = new_scores - old_scores
    for i, agent in enumerate(agents):
        agent.observe(rewards[i], gs.is_game_over(), i)


def run_to_the_end(agents: List[Agent], gs: GameState):
    while not gs.is_game_over():
        run_step(agents, gs)


def run_for_n_games_and_return_stats(agents: List[Agent], gs: GameState, games_count: int) -> (np.ndarray, np.ndarray):
    total_scores = np.zeros_like(gs.get_scores())

    for _ in range(games_count):
        gs_copy = gs.clone()
        run_to_the_end(agents, gs_copy)
        total_scores += gs_copy.get_scores()

    return total_scores, total_scores / games_count


def run_for_n_games_and_print_stats(agents: List[Agent], gs: GameState, games_count: int):
    total_scores, mean_scores = run_for_n_games_and_return_stats(agents, gs, games_count)

    print(f"Total Scores : {total_scores}")
    print(f"Mean Scores : {mean_scores}")


def run_for_n_games_and_return_max(agents: List[Agent], gs: GameState, games_count: int) -> np.ndarray:
    old_and_new_scores = np.ones((2, len(gs.get_scores()))) * -9999.9

    for _ in range(games_count):
        gs_copy = gs.clone()
        run_to_the_end(agents, gs_copy)
        new_scores = gs_copy.get_scores()
        old_and_new_scores[1, :] = new_scores
        old_and_new_scores[0, :] = np.max(old_and_new_scores, axis=0)

    return old_and_new_scores[0, :]

def run_for_n_games_and_print_stats_1(agents: List[Agent], gs: GameState, games_count: int, name):
    start = timeit.default_timer()
    total_scores, mean_scores = run_for_n_games_and_return_stats(agents, gs, games_count)
    stop = timeit.default_timer()
    f = open("result.txt", "a")
    f.write(name + ';')
    f.write(str(stop - start) + ';')
    f.write(str(total_scores[0]) + ';' + str(total_scores[1]) + ';')
    f.write(str(mean_scores[0]) + ';' + str(mean_scores[1]) + ';')
    f.write('\n')
    f.close()
    print('Time: ', stop - start)
    print(f"Total Scores : {total_scores}")
    print(f"Mean Scores : {mean_scores}")