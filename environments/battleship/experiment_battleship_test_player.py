
from environments.battleship import BattleshipGameState

if __name__ == "__main__":
    gs = BattleshipGameState()
    gs.put_all_boat()
    print(gs.board_j1)
    print()
    print(gs.board_j2)
