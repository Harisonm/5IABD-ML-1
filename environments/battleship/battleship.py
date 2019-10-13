# import os
from typing import List
import random
import numpy as np

from contracts import GameState


# Chaque joueur possède les mêmes navires, dont le nombre et le type dépendent des règles du jeu choisies.

# Une disposition peut ainsi comporter :

# 1 porte-avions (5 cases)
# 1 croiseur (4 cases)
# 2 contre-torpilleurs (3 cases)
# 1 torpilleur (2 cases)

class BattleshipGameState(GameState):

    def __init__(self):
        self.board_j1 = np.zeros((10, 10), dtype=int)
        self.board_attack_j1 = np.zeros((10, 10), dtype=int)
        self.board_j2 = np.zeros((10, 10), dtype=int)
        self.board_attack_j2 = np.zeros((10, 10), dtype=int)

        self.game_over = False
        self.scores = np.zeros(2)
        self.available_actions = [5, 4, 3, 3, 2]  # porte-avions croiseur contre-torpilleurs torpilleur
        self.attack_actions = [1]  # Attack
        self.remaining_actions = 50
        self.active_player = 0
        self.boat_vector = {
            5: np.array([5, 5, 5, 5, 5]),
            4: np.array([4, 4, 4, 4]),
            3: np.array([3, 3, 3]),
            2: np.array([2, 2]),
        }

    def player_count(self) -> int:
        return 2

    def is_game_over(self) -> bool:
        return self.game_over

    def get_active_player(self) -> int:
        return self.active_player

    def clone(self) -> 'GameState':
        gs_clone = BattleshipGameState()
        gs_clone.game_over = self.game_over
        gs_clone.attack_actions = self.attack_actions
        gs_clone.active_player = self.active_player
        gs_clone.scores = self.scores.copy()
        gs_clone.available_actions = self.available_actions.copy()
        gs_clone.board_j1 = self.board_j1.copy()
        gs_clone.board_attack_j1 = self.board_attack_j1.copy()
        gs_clone.board_j2 = self.board_j2.copy()
        gs_clone.board_attack_j2 = self.board_attack_j2.copy()
        return gs_clone

    def step(self, player_index: int, action_index: int):
        assert (not self.game_over)
        assert (player_index == self.active_player)
        return 0

    def put_boat_and_save_position(self, boat_type: int, plateau: str):
        vh = random.randint(0, 1)  # 0 : vertical -/- 1 : horizontal
        relative_position = random.randint(0, (9 - boat_type))  # position max by boat size
        pos = random.randint(0, 9)
        if vh:
            if np.sum(vars(self)[plateau][relative_position: relative_position + boat_type, pos: pos + 1]) == 0:
                vars(self)[plateau][relative_position: relative_position + boat_type, pos: pos + 1] = self.boat_vector[
                    boat_type].reshape(boat_type, 1)
            else:
                self.put_boat_and_save_position(boat_type, plateau)
        else:
            if np.sum(vars(self)[plateau][pos: pos + 1, relative_position: relative_position + boat_type]) == 0:
                vars(self)[plateau][pos: pos + 1, relative_position: relative_position + boat_type] = self.boat_vector[
                    boat_type]
            else:
                self.put_boat_and_save_position(boat_type, plateau)

    def put_all_boat(self):
        for x in self.available_actions:
            self.put_boat_and_save_position(x, 'board_j1')
            self.put_boat_and_save_position(x, 'board_j2')

    def attack_boat(self):
        pass

    def check_boat(self):
        pass

    def get_scores(self) -> np.ndarray:
        pass

    def get_available_actions(self, player_index: int) -> List[int]:
        pass

    def __str__(self):
        pass

    def get_unique_id(self) -> int:
        pass

    def get_max_state_count(self) -> int:
        pass

    def get_action_space_size(self) -> int:
        pass

    def get_vectorized_state(self) -> np.ndarray:
        pass

    # board = np.array([
    #     [2, 2, 0, 0, 0, 0, 4, 4, 4, 4],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    #     [4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    #     [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [4, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    #     [2, 2, 0, 0, 0, 0, 0, 0, 0, 3],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 5, 5, 5, 5, 5]
    # ])
    #
    # board_attack = np.array([
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    #     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ])
