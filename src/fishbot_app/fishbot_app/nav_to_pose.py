'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-16 02:53:56
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-16 03:05:57
FilePath: /fish_bot_ws/src/fishbot_app/fishbot_app/nav_to_pose.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()

    navigator = BasicNavigator()
    navigator.waitUntilNav2Active()

    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = 2.0
    pose.pose.position.y = 1.0
    pose.pose.orientation.w = 1.0

    navigator.goToPose(pose)

    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        navigator.get_logger().info(
            f'预计: {Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9} s 后到达')
        if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
            navigator.cancelTask()

    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        navigator.get_logger().info('导航结果：成功')
    elif result == TaskResult.CANCELED:
        navigator.get_logger().warn('导航结果：被取消')
    elif result == TaskResult.FAILED:
        navigator.get_logger().error('导航结果：失败')
    else:
        navigator.get_logger().error('导航结果：返回状态无效')

    rclpy.shutdown()

if __name__ == '__main__':
    main()