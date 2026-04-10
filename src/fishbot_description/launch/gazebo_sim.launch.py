'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-03-24 18:10:27
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-10 15:39:29
FilePath: /fish_bot_ws/src/fishbot_description/launch/display_robot.launch.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import launch
from launch.event_handlers import OnProcessExit
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess,RegisterEventHandler
from launch_ros.actions import Node

from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    # 获取功能包的share路径
    package_share_directory = get_package_share_directory('fishbot_description')
    xacro_path = os.path.join(package_share_directory, 'urdf', 'fishbot/fishbot.urdf.xacro')
    gazebo_world_path = os.path.join(package_share_directory, 'world', 'remote_fishbot_room.world')

    # rviz_config_path = os.path.join(package_share_directory, 'config', 'lesson1.rviz')
    # gazebo会自动拉起对应的rviz2节点，所以不需要再拉起rviz2节点

    #声明launch文件参数（名称、默认值、描述）
    declare_model_arg = DeclareLaunchArgument(
        'model',
        default_value=xacro_path,
        description='URDF model path'
    )

    command_result = Command(['xacro ',LaunchConfiguration('model')])
    robot_description = ParameterValue(command_result, value_type=str)

    robot_state_publisher_node = Node( 
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )
    
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            get_package_share_directory('gazebo_ros') + '/launch/gazebo.launch.py'),
            launch_arguments={'world': gazebo_world_path, 'verbose': 'true'}.items()
    )
    
    # 加载机器人到gazebo仿真环境中
    spawn_entity_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'fishbot']
    )

    # 加载joint_state的控制器
    load_joint_state_controller_node = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'fishbot_joint_state_broadcaster'],
        output='screen'
    )

    # 加载effort的控制器
    # load_effort_controller_node = ExecuteProcess(
    #     cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'fishbot_effort_controller'],
    #     output='screen'
    # )

    # 加载diff_drive的控制器
    load_diff_drive_controller_node = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'fishbot_diff_drive_controller'],
        output='screen'
    )
    
    return launch.LaunchDescription([
        declare_model_arg,
        robot_state_publisher_node,
        gazebo_launch,
        spawn_entity_node,
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=spawn_entity_node,
                on_exit=[load_joint_state_controller_node]
            )
        ),
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=load_joint_state_controller_node,
                on_exit=[load_diff_drive_controller_node]
            )
        ),
    ])
