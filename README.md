# MTAC: Hierachical Reinforcement Learning-based Multi-gait Terrain-adpative Quadruped Controller
This repository provides an implementation of the paper: "MTAC: Hierachical Reinforcement Learning-based Multi-gait Terrain-adpative Quadruped Controller," by Nishaant Shah, and Aniket Bera.

This work uses NVIDIA's Isaac Gym simulator (Paper: https://arxiv.org/abs/2108.10470), builds on the legged gym environment by Nikita Rudin, Robotic Systems Lab, ETH Zurich (Paper: https://arxiv.org/abs/2109.11978), and training code from the rsl_rl repository, by Nikita Rudin, Robotic Systems Lab, ETH Zurich. All redistributed and/or modified code retains its original license.

System Requirements:
1. Python 3.8
2. pytorch 1.10 with cuda-11.3
3. Isaac Gym Preview 4 (https://developer.nvidia.com/isaac-gym)
4. PPO Implementation: rsl_rl, found at https://github.com/leggedrobotics/rsl_rl
5. NVIDIA GPU

Model overview:
![method (1)](https://github.com/nshah067/hierarchical-locomotion/assets/60299940/3975bee7-2f7e-41ac-a2d6-e33ec8a65e69)

Paper: https://arxiv.org/abs/2401.03337
