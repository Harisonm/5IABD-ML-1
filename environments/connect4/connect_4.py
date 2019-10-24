from typing import List

import os

import numpy as np

from contracts import GameState


class Connect4GameState(GameState):
    def __init__(self):
        self.game_over = False
        self.active_player = 0
        self.scores = np.zeros(2)
        self.available_actions = [0, 1, 2, 3, 4, 5, 6]  # nb col
        self.board = np.ones((6, 7), dtype=np.int) * -1

    def player_count(self) -> int:
        return 2

    def is_game_over(self) -> bool:
        return self.game_over

    def get_active_player(self) -> int:
        return self.active_player

    def clone(self) -> 'GameState':
        gs_clone = Connect4GameState()
        gs_clone.game_over = self.game_over
        gs_clone.active_player = self.active_player
        gs_clone.scores = self.scores.copy()
        gs_clone.available_actions = self.available_actions.copy()
        gs_clone.board = self.board.copy()
        return gs_clone

    def array_contains_four(self, array):
        count = 0
        i = 0
        len_a = len(array)
        while count < 4 and i < (len_a - 1):
            if array[i] != -1 and array[i] == array[i + 1]:
                count = count + 1
                if count == 3:
                    return True
            else:
                count = 0
            i = i + 1
        if count == 3:
            return True
        else:
            return False

    def contains_four(self, action_i: int, action_j: int):
        arrays = [self.board[action_i, :],
                  self.board[:, action_j],
                  np.diagonal(self.board, (action_j - action_i)),
                  np.diagonal(np.flip(self.board, 1), 6 - (action_j + action_i))]

        for a in arrays:
            boolean_contains_four = self.array_contains_four(a)
            if boolean_contains_four:
                return True
        return False

    def step(self, player_index: int, action_index: int):
        assert (not self.game_over)
        assert (player_index == self.active_player)
        assert (0 <= action_index <= 6)
        assert (self.board[0, action_index] == -1)  # on verifie qu'il y a des case vides sur cette col

        wanted_j = action_index
        i = 5  # LA LIGNE 5 EST EN BAS ET LA LIGNE 0 EST EN HAUT
        while self.board[i, wanted_j] != -1 and i >= 0:
            i = i - 1
        wanted_i = i

        potential_cell_type = self.board[wanted_i, wanted_j]
        assert (potential_cell_type == -1)

        self.board[wanted_i, wanted_j] = player_index

        if self.board[0, action_index] != -1:
            self.available_actions.remove(action_index)

        if self.contains_four(wanted_i, wanted_j):
            self.game_over = True
            self.scores[player_index] = 1
            self.scores[(player_index + 1) % 2] = -1
            return

        # Passer la main à l'autre joueur
        for i in range(5):
            for j in range(6):
                if self.board[i, j] == -1:
                    self.active_player = (self.active_player + 1) % 2
                    return

        self.game_over = True
        return

    def get_scores(self) -> np.ndarray:
        return self.scores

    def get_available_actions(self, player_index: int) -> List[int]:
        return self.available_actions

    def __str__(self):
        str_acc = f"Game Over : {self.game_over}{os.linesep}"
        str_acc += f"Remaining Actions : {self.available_actions}{os.linesep}"
        str_acc += f"Scores : {self.scores}{os.linesep}"

        for i, line in enumerate(self.board):
            for j, cell_type in enumerate(line):
                if cell_type == -1:
                    str_acc += "-"
                elif cell_type == 0:
                    str_acc += "X"
                else:
                    str_acc += "O"
            str_acc += f"{os.linesep}"

        return str_acc

    def get_unique_id(self) -> int:
        acc = 0
        for i in range(42):
            acc += (3 ** i) * (self.board[i // 7, i % 7] + 1)
        return acc

    def get_max_state_count(self) -> int:
        return 3 ** 42

    def get_action_space_size(self) -> int:
        return 7

    def get_vectorized_state(self) -> np.ndarray:
        state_vec = np.zeros(3 * 6 * 7)
        for i in range(6):
            for j in range(7):
                state_vec[i * 7 * 3 + j * 3 + (self.board[i, j] + 1)] = 1
        return state_vec


if __name__ == "__main__":
    gs = Connect4GameState()
    print(gs)
