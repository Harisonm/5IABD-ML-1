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


def run_for_n_games_and_print_stats(agents: List[Agent], gs: GameState, games_count: int):
    total_scores = np.zeros_like(gs.get_scores())

    for _ in range(games_count):
        gs_copy = gs.clone()
        run_to_the_end(agents, gs_copy)
        total_scores += gs_copy.get_scores()

    print(f"Total Scores : {total_scores}")
    print(f"Mean Scores : {total_scores/games_count}")
