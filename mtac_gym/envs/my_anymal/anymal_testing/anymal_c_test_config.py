from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class AnymalCTestCfg( LeggedRobotCfg ):
    class env( LeggedRobotCfg.env ):
        num_envs = 1
        num_actions = 12
        episode_length = 25
    class commands(LeggedRobotCfg.commands):
        curriculum = False
        max_curriculum = 1.
        num_commands = 4 # default: lin_vel_x, lin_vel_y, ang_vel_yaw, heading (in heading mode ang_vel_yaw is recomputed from heading error)
        resampling_time = 100000. # time before command are changed[s]
        heading_command = True # if true: compute ang vel command from heading error
        class ranges:
            lin_vel_x = [1.5,1.5] # min max [m/s]
            lin_vel_y = [0.0,0.0]
            ang_vel_yaw = [-1, 1]    # min max [rad/s]
            heading = [1.57,1.57]

    class terrain( LeggedRobotCfg.terrain ):
        mesh_type = 'trimesh'
        horizontal_scale = 0.1 # [m]
        vertical_scale = 0.005 # [m]
        # terrain types: [smooth slope, rough slope, stairs up, stairs down, discrete]
        #terrain_proportions = [0, 0, 1, 0, 0]
        curriculum = False
        selected = False
        num_rows= 5 # number of terrain rows (levels)
        num_cols = 5 # number of terrain cols 
        terrain_kwargs = {'type':'pyramid2'}

    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.6] # x,y,z [m]
        rot = [0.0, 0.0, 0.0, 0.5] # x,y,z,w [quat]
        default_joint_angles = { # = target angles [rad] when action = 0.0
            "LF_HAA": 0.0,
            "LH_HAA": 0.0,
            "RF_HAA": -0.0,
            "RH_HAA": -0.0,

            "LF_HFE": 0.4,
            "LH_HFE": -0.4,
            "RF_HFE": 0.4,
            "RH_HFE": -0.4,

            "LF_KFE": -0.8,
            "LH_KFE": 0.8,
            "RF_KFE": -0.8,
            "RH_KFE": 0.8,
        }

    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        stiffness = {'HAA': 80., 'HFE': 80., 'KFE': 80.}  # [N*m/rad]
        damping = {'HAA': 2., 'HFE': 2., 'KFE': 2.}     # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.5
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4
        use_actuator_network = True
        actuator_net_file = "{LEGGED_GYM_ROOT_DIR}/resources/actuator_nets/anydrive_v3_lstm.pt"

    class asset( LeggedRobotCfg.asset ):
        file = "{LEGGED_GYM_ROOT_DIR}/resources/robots/anymal_c/urdf/anymal_c.urdf"
        name = "anymal_c"
        foot_name = "FOOT"
        penalize_contacts_on = ["SHANK", "THIGH"]
        terminate_after_contacts_on = ["base"]
        self_collisions = 1 # 1 to disable, 0 to enable...bitwise filter

    class domain_rand( LeggedRobotCfg.domain_rand):
        randomize_base_mass = False
        added_mass_range = [-5., 5.]
  
    class rewards( LeggedRobotCfg.rewards ):
        base_height_target = 0.5
        max_contact_force = 500.
        only_positive_rewards = True
        class scales( LeggedRobotCfg.rewards.scales ):
            pass

class AnymalCTestCfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = 'test'
        experiment_name = 'test_anymal_c'
        num_steps_per_env = 500
