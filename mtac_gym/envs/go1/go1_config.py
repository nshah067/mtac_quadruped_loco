from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class AnymalCPyraCfg( LeggedRobotCfg ):
    class env( LeggedRobotCfg.env ):
        #Lets add here and maybe even start fresh
        num_envs = 2000
        num_observations = 100
        episode_length_s = 20

    class terrain( LeggedRobotCfg.terrain ):
        print("Im cooking rn")
        border_size = 10
        static_friction = 1.0
        dynamic_friction = 1.0
        #Lets make this more efficient and parameterized. Start fresh here.

    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0, 0.0, 0.34]  # x,y,z [m]
        default_joint_angles = {  # = target angles [rad] when action = 0.0
            'FL_hip_joint': 0.1,  # [rad]
            'RL_hip_joint': 0.1,  # [rad]
            'FR_hip_joint': -0.1,  # [rad]
            'RR_hip_joint': -0.1,  # [rad]

            'FL_thigh_joint': 0.8,  # [rad]
            'RL_thigh_joint': 1.,  # [rad]
            'FR_thigh_joint': 0.8,  # [rad]
            'RR_thigh_joint': 1.,  # [rad]

            'FL_calf_joint': -1.5,  # [rad]
            'RL_calf_joint': -1.5,  # [rad]
            'FR_calf_joint': -1.5,  # [rad]
            'RR_calf_joint': -1.5  # [rad]
        }

    class commmands(LeggedRobotCfg.commands):
        #Lets refresh here as well.
        lin_vel_x = [-1.0, 1.0]
        lin_vel_y = [-1.0, 1.0]
        heading_command = False
        resampling_time = 10.0
        command_curriculum = True
        num_lin_vel_bins = 30
        num_ang_vel_bins = 30
        ang_vel_yaw = [-1, 1]
        
    class control( LeggedRobotCfg.control ):
        control_type = 'P'
        stiffness = {'joint': 20.}  # [N*m/rad]
        damping = {'joint': 0.5}  # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.25
        hip_scale_reduction = 0.5
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        foot_name = "foot"
        penalize_contacts_on = ["thigh", "calf"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 0  # 1 to disable, 0 to enable
        flip_visual_attachments = False
        fix_base_link = False
        file = "{LEGGED_GYM_ROOT_DIR}/resources/robots/go1/urdf/go1.urdf"
        name = "go1"

    class domain_rand( LeggedRobotCfg.domain_rand):
        randomize_base_mass = True
        added_mass_range = [-3., 3.]
        push_robots = False
        max_push_vel_xy = 0.5
        randomize_friction = True
        friction_range = [0.05, 4.5]
        randomize_restitution = True
        restitution_range = [0.0, 1.0]
        restitution = 0.5  # default terrain restitution
        randomize_com_displacement = True
        com_displacement_range = [-0.1, 0.1]
        randomize_motor_strength = True
        motor_strength_range = [0.9, 1.1]
        randomize_Kp_factor = False
        Kp_factor_range = [0.8, 1.3]
        randomize_Kd_factor = False
        Kd_factor_range = [0.5, 1.5]
        rand_interval_s = 6
  
    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.5

        class reward_scales(LeggedRobotCfg.rewards.scales):
            #Lets cook something up here nish
            torques = -0.0001
            action_rate = -0.01
            dof_pos_limits = -10.0
            orientation = -5.
            base_height = -30.

class AnymalCPyraCfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = 'go1_run'
        experiment_name = 'go1_experiment'
        resume = False
        load_run = -1
