# SPDX-FileCopyrightText: Copyright (c) 2021 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2021 ETH Zurich, Nikita Rudin

from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR
from .base.legged_robot import LeggedRobot
from .anymal_c.anymal import Anymal
from .anymal_c.mixed_terrains.anymal_c_rough_config import AnymalCRoughCfg, AnymalCRoughCfgPPO
from .anymal_c.flat.anymal_c_flat_config import AnymalCFlatCfg, AnymalCFlatCfgPPO
#my change
from .my_anymal.anymal_c_stairpit.anymal_c_stairpit_config import AnymalCPyrCfg, AnymalCPyrCfgPPO
from .my_anymal.anymal_c_pyramid.anymal_c_pyramid_config import AnymalCPyraCfg, AnymalCPyraCfgPPO
from .my_anymal.anymal_c_uneven.anymal_c_uneven_config import AnymalCUnevenCfg, AnymalCUnevenCfgPPO
from .my_anymal.anymal_c_step.anymal_c_step_config import AnymalCStepCfg, AnymalCStepCfgPPO
from .my_anymal.anymal_testing.anymal_c_test_config import AnymalCTestCfg, AnymalCTestCfgPPO

import os

from legged_gym.utils.task_registry import task_registry

task_registry.register( "anymal_c_rough", Anymal, AnymalCRoughCfg(), AnymalCRoughCfgPPO() )
task_registry.register( "anymal_c_flat", Anymal, AnymalCFlatCfg(), AnymalCFlatCfgPPO() )

#my change
task_registry.register("anymal_c_pyramid", Anymal, AnymalCPyraCfg(), AnymalCPyraCfgPPO())
task_registry.register("anymal_c_stairpit", Anymal, AnymalCPyrCfg(), AnymalCPyrCfgPPO())
task_registry.register("anymal_c_uneven", Anymal, AnymalCUnevenCfg(), AnymalCUnevenCfgPPO())
task_registry.register("anymal_c_step", Anymal, AnymalCStepCfg(), AnymalCStepCfgPPO())
task_registry.register("anymal_c_test", Anymal, AnymalCTestCfg(), AnymalCTestCfgPPO())
