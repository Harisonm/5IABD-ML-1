import os
from typing import List

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
        self.world = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        self.player_pos = np.array([1, 1])
        self.game_over = False
        self.scores = np.array([0], dtype=np.float)
        self.available_actions = [5, 4, 3, 2]  # porte-avions croiseur contre-torpilleurs torpilleur
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
        gs_clone.board = self.world.copy()
        gs_clone.board_attack = self.world.copy()
        return gs_clone

    def step(self, player_index: int, action_index: int):
        assert (not self.game_over)
        assert (player_index == self.active_player)
        return 0

    
    def put_boat_and_save_position(self,boat_type : int, player_index:int, action_type: int,action_index : int, begin: int, end : int):
        assert(not self.active_player)
        assert(not self.action_index)
        boat_position = np.array([])
        if action_type == 1:
            # Soit en vertical
            self.board[begin:end, (action_index-1):action_index] = self.boat_vector[boat_type]
            boat_position = []
        else :
            # Soit en horizontal
            self.board[(action_index-1):action_index, begin:end] = self.boat_vector[boat_type]
            
    def attack_boat(self):
        pass
        
        
    def check_boat(self):
        pass
    
board = np.array([
        [2, 2, 0, 0, 0, 0, 4, 4, 4, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 5, 5, 5, 5]
    ])

board_attack = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])