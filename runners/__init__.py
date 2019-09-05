from typing import List

from contracts import Agent, GameState


def run_step(agents: List[Agent], gs: GameState):
    assert (not gs.is_game_over())
    active_player_index = gs.get_active_player()
    action = agents[active_player_index].act(gs)
    gs.step(active_player_index, action)


def run_to_the_end(agents: List[Agent], gs: GameState):
    while not gs.is_game_over():
        run_step(agents, gs)
