from tensorflow.python.keras.metrics import *
from tensorflow.python.keras.utils import *

from brains import DQNBrain
from contracts import Agent, GameState


# si gs1 == gs2 => hash(gs1) == hash(gs2)
# si gs1 != gs2 => hash(gs1) != hash(gs2) || hash(gs1) == hash(gs2)


class PPOAgent(Agent):
    def __init__(self,
                 action_space_size: int,
                 alpha: float = 0.01,
                 gamma: float = 0.999,
                 epsilon: float = 0.1,
                 episodes_count_between_training: int = 100,

                 ):
        self.action_space_size = action_space_size
        self.episodes_count_between_training = episodes_count_between_training
        self.s = []
        self.a = []
        self.r = []
        self.v = []
        self.m = []
        self.r_temp = 0.0
        self.is_last_episode_terminal = True
        self.current_episode_count = 0
        self.buffer = {
            'states': [],
            'chosen_actions': [],
            'gains': [],
            'advantages': [],
            'masks': []
        }
        self.gamma = gamma
        self.epsilon = epsilon

    def act(self, gs: GameState) -> int:
        #gs_unique_id = gs.get_unique_id()
        available_actions = gs.get_available_actions(gs.get_active_player())

        state_vec = gs.get_vectorized_state()

        chosen_action = np.random.choice(available_actions)
        self.v.append(0.0)
        self.s.append(state_vec)
        self.a.append(to_categorical(chosen_action, self.action_space_size))
        if not self.is_last_episode_terminal:
            self.r.append(self.r_temp)
        self.r_temp = 0.0

        return chosen_action

    def observe(self, r: float, t: bool, player_index: int):
        if self.is_last_episode_terminal:
            return

        self.r_temp += r

        if t:
            self.current_episode_count += 1
            self.r.append(self.r_temp)
            self.compute_gains_and_advantages()
            if self.current_episode_count == self.episodes_count_between_training:
                self.train()
                self.buffer['states'].clear()
                self.buffer['chosen_actions'].clear()
                self.buffer['gain'].clear()
                self.buffer['advantages'].clear()
                self.buffer['masks'].clear()
            self.s.clear()
            self.a.clear()
            self.r.clear()
            self.v.clear()
            self.m.clear()
            self.r_temp = 0.0
            self.is_last_episode_terminal = True

    def compute_gains_and_advantages(self):

        last_gain = 0.0
        for i in reversed(range(len(self.s))):
            last_gain = self.r[i] + self.gamma * last_gain
            self.buffer['states'].append(self.s[i])
            self.buffer['chosen_actions'].append(self.a[i])
            self.buffer['gain'].append(last_gain)
            self.buffer['advantages'].append(last_gain - self.v[i])
            self.buffer['masks'].append(self.m[i])
