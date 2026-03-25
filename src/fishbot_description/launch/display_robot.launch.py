'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-03-24 18:10:27
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-03-25 15:46:34
FilePath: /fish_bot_ws/src/fishbot_description/launch/display_robot.launch.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    # 获取urdf路径
    package_share_directory = get_package_share_directory('fishbot_description')
    urdf_path = os.path.join(package_share_directory, 'urdf', 'first_robot.urdf')
    xacro_path = os.path.join(package_share_directory, 'urdf', 'first_robot.xacro')
    rviz_config_path = os.path.join(package_share_directory, 'config', 'lesson1.rviz')
    #声明launch文件参数（名称、默认值、描述）
    action_declare_arg_mode_path = DeclareLaunchArgument(
        'model',
        default_value=urdf_path,
        description='URDF model path'
    )

    # command_result = Command(['cat ',LaunchConfiguration('model')])
    command_result = Command(['xacro ',LaunchConfiguration('model')])
    robot_description = ParameterValue(command_result, value_type=str)

    robot_state_pub = Node( 
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )
    
    joint_state_pub = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )
    
    rivz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config_path]
    )

    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        robot_state_pub,
        joint_state_pub,
        rivz_node,
    ])
