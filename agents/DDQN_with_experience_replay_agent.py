import random
from tensorflow.python.keras.metrics import *
from tensorflow.python.keras.utils import *

from brains import DQNBrain
from contracts import Agent, GameState
from collections import deque


# si gs1 == gs2 => hash(gs1) == hash(gs2)
# si gs1 != gs2 => hash(gs1) != hash(gs2) || hash(gs1) == hash(gs2)


class DDQNAgentWithER(Agent):
    def __init__(self,
                 hidden_layers: int,
                 neurons_per_hidden_layer: int,
                 action_space_size: int,
                 alpha: float = 0.01,
                 gamma: float = 0.999,
                 epsilon: float = 1,
                 epsilon_decay: float = 0.995,
                 epsilon_min: float = 0.01,
                 batch_size: int = 32,
                 ):
        self.Q = DQNBrain(output_dim=action_space_size, learning_rate=alpha,
                          hidden_layers_count=hidden_layers,
                          neurons_per_hidden_layer=neurons_per_hidden_layer)
        self.alternate_Q = DQNBrain(output_dim=action_space_size, learning_rate=alpha,
                                    hidden_layers_count=hidden_layers,
                                    neurons_per_hidden_layer=neurons_per_hidden_layer)
        self.action_space_size = action_space_size
        self.s = None
        self.a = None
        self.r = None
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size
        self.memory = deque(maxlen=20000)
        self.remember(self.s, self.s, self.a, self.r, True)

    def remember(self, state, next_state, action, reward, done):
        """
        remember the experience
        :param state:
        :param next_state:
        :param action:
        :param reward:
        :param done:
        :return:
        """
        self.memory.append((state, next_state, action, reward, done))

    def act(self, gs: GameState) -> int:
        available_actions = gs.get_available_actions(gs.get_active_player())
        state_vec = gs.get_vectorized_state()
        predicted_Q_values = self.Q.predict(state_vec)
        if np.random.random() <= self.epsilon:
            chosen_action = np.random.choice(available_actions)
        else:
            chosen_action = available_actions[int(np.argmax(predicted_Q_values[available_actions]))]
        batch = random.choices(self.memory, k=self.batch_size)
        for state, next_state, action, reward, done in batch:
            target = reward
            if not done:
                if self.s is not None:
                    target = target + self.gamma * self.alternate_Q.predict(state_vec)[available_actions][
                        np.argmax(self.Q.predict(state_vec)[available_actions])]
                    self.Q.train(self.s, self.a, target)
                    self.remember(self.s, state_vec, self.a, self.r, True)
        self.s = state_vec
        self.a = to_categorical(chosen_action, self.action_space_size)
        self.r = 0.0
        return chosen_action

    def observe(self, r: float, t: bool, player_index: int):
        if self.r is None:
            return

        self.r += r

        if t:
            target = self.r
            self.Q.train(self.s, self.a, target)
            self.s = None
            self.a = None
            self.r = None
