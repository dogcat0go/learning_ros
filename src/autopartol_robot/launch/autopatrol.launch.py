'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-22 23:31:33
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-22 23:51:01
FilePath: /fish_bot_ws/src/autopartol_robot/launch/autopatrol.launch.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # 获取与拼接默认路径
    autopatrol_robot_dir = get_package_share_directory(
        'autopartol_robot')
    patrol_config_path = os.path.join(
        autopatrol_robot_dir, 'config', 'patrol_config.yaml')
    
    action_node_turtle_control = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='patrol_node',
        parameters=[patrol_config_path]
    )
    speaker_node = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='speaker',
    )

    return launch.LaunchDescription([
        action_node_turtle_control,
        speaker_node,
    ])