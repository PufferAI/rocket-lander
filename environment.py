from pdb import set_trace as T
import functools

import pufferlib
import pufferlib.emulation
import pufferlib.postprocess
import pufferlib.wrappers

def env_creator(name='rocketlander'):
    return functools.partial(make, name)

def make(name, render_mode='rgb_array'):
    '''Atari creation function'''
    settings = {'Side Engines': True,
                'Clouds': True,
                'Vectorized Nozzle': True,
                'Starting Y-Pos Constant': 1,
                'Initial Force': 'random'}  # (6000, -10000)}

    from .environments.rocketlander import RocketLander
    env = RocketLander(settings)
    env = pufferlib.wrappers.GymToGymnasium(env)
    env = pufferlib.postprocess.EpisodeStats(env)
    env = pufferlib.emulation.GymnasiumPufferEnv(env=env)
    return env
