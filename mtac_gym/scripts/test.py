import numpy as np
import os
from datetime import datetime

import isaacgym
from legged_gym.envs import *
from legged_gym.utils import  get_args, export_policy_as_jit, task_registry, Logger

import torch


def test(args):
    env_cfg, train_cfg = task_registry.get_cfgs(name=args.task)
    
    # override some parameters for testing
    env_cfg.env.num_envs = 1
    env_cfg.terrain.num_rows = 5
    env_cfg.terrain.num_cols = 1
    env_cfg.terrain.curriculum = False
    env_cfg.noise.add_noise = False
    env_cfg.domain_rand.randomize_friction = False
    env_cfg.domain_rand.push_robots = False
    env_cfg.max_episode_length = 500
    # prepare environment
    #env, _ = task_registry.make_env(name=args.task, args=args, env_cfg=env_cfg)
    
    env, _ = task_registry.make_env('anymal_c_test', args=args, env_cfg=env_cfg)
    obs = env.get_observations()
    
    train_cfg.runner.resume = True
    ppo_runner, train_cfg = task_registry.make_alg_runner(env=env, name=args.task, args=args, train_cfg=train_cfg)
    policy = ppo_runner.get_inference_policy(device=env.device)
    
    while True:
        actions = policy(obs.detach())
        obs, _, rew, done, info = env.step(actions)
    print("Done")

if __name__ == '__main__':
    args = get_args()
    test(args)