import gym
from gym.utils.play import play

play(gym.make("Breakout-v4", render_mode='human'), zoom=3)