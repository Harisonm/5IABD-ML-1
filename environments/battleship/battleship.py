# import os
from typing import List
import random
import numpy as np

from contracts import GameState


class BattleshipGameState(GameState):

    def __init__(self):
        self.board_j0 = np.zeros((10, 10), dtype=int) * -1
        self.board_attack_j0 = np.zeros((10, 10), dtype=int) * -1
        self.board_j1 = np.zeros((10, 10), dtype=int) * -1
        self.board_attack_j1 = np.zeros((10, 10), dtype=int) * -1

        self.game_over = False
        self.scores = np.zeros(2)
        self.available_actions = [5, 4, 3, 3, 2]
        self.remaining_boat = [17, 17]
        self.remaining_action = [[a for a in range(100)] for x in range(2)]
        self.active_player = 0
        self.boat_vector = {
            5: np.array([5, 5, 5, 5, 5]),
            4: np.array([4, 4, 4, 4]),
            3: np.array([3, 3, 3]),
            2: np.array([2, 2]),
        }
        self.put_all_boat()


    def player_count(self) -> int:
        return 2

    def is_game_over(self) -> bool:
        return self.game_over

    def get_active_player(self) -> int:
        return self.active_player

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
            self.put_boat_and_save_position(x, 'board_j0')
            self.put_boat_and_save_position(x, 'board_j1')

    def step(self, player_index: int, action_index: int):
        assert (not self.game_over)
        assert (player_index == self.active_player)

        (wanted_i, wanted_j) = (action_index // 10, action_index % 10)
        potential_cell_type = vars(self)['board_attack_j' + str(player_index)][wanted_i, wanted_j]
        assert (potential_cell_type == 0)

        vars(self)['board_attack_j' + str(player_index)][wanted_i, wanted_j] = \
            vars(self)['board_j' + str(player_index + 1 % 2)][wanted_i, wanted_j] if \
            vars(self)['board_j' + str(player_index + 1 % 2)][wanted_i, wanted_j] != -1 else 9
        if vars(self)['board_attack_j' + str(player_index)][wanted_i, wanted_j] != 9:
            self.remaining_boat[player_index] -= 1

        print(f'player index : {player_index}')
        print(vars(self)['board_attack_j' + str(player_index)])

        self.remaining_action[player_index].remove(action_index)
        print(action_index)

        if self.remaining_boat[player_index] == 0:
            self.game_over = True
        return

    def get_scores(self) -> np.ndarray:
        return self.scores

    def get_available_actions(self, player_index: int) -> List[int]:
        return self.available_actions

    def __str__(self):
        pass

    def get_unique_id(self) -> int:
        acc = 0
        for i in range(100):
            acc += (6 ** i) * (vars(self)['board_attack_j' + str(self.active_player)][i // 10, i % 10] + 1)
        return acc

    def get_max_state_count(self) -> int: # -1 : nothing , 5,4,3,2 : boats, 9 : missed
        return 6 ** 100

    def get_action_space_size(self) -> int:
        return 100

    def get_vectorized_state(self) -> np.ndarray:
        pass

    def clone(self) -> 'GameState':
        gs_clone = BattleshipGameState()
        gs_clone.game_over = self.game_over
        gs_clone.active_player = self.active_player
        gs_clone.scores = self.scores.copy()
        gs_clone.remaining_action = self.remaining_action.copy()
        gs_clone.board_j0 = self.board_j0.copy()
        gs_clone.board_attack_j0 = self.board_attack_j0.copy()
        gs_clone.board_j1 = self.board_j1.copy()
        gs_clone.board_attack_j1 = self.board_attack_j1.copy()
        gs_clone.remaining_boat = self.remaining_boat.copy()
        return gs_clone
