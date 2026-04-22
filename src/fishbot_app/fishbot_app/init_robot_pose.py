'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-14 05:23:51
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-16 03:28:39
FilePath: /fish_bot_ws/src/fishbot_app/fishbot_app/init_robot_pose.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""Nav2 node that sets the robot initial pose on the map frame."""
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy


class InitRobotPose(BasicNavigator):
    """Single Nav2 node: BasicNavigator is already an rclpy Node."""

    def __init__(self):
        super().__init__(node_name='init_robot_pose')
        self.initial_pose = PoseStamped()
        self.initial_pose.header.frame_id = 'map'
        self.initial_pose.header.stamp = self.get_clock().now().to_msg()
        self.initial_pose.pose.position.x = 0.0
        self.initial_pose.pose.position.y = 0.0
        self.initial_pose.pose.orientation.w = 1.0
        # self.wait_for_server(timeout=20.0)
        self.setInitialPose(self.initial_pose)
        self.waitUntilNav2Active()

    def get_initial_pose(self):
        return self.initial_pose

def main():
    rclpy.init()
    node = InitRobotPose()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        # spin() may already shut down the context on SIGINT; avoid double shutdown.
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
