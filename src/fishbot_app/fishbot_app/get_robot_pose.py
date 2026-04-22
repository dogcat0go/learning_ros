'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-15 23:29:09
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-15 23:32:41
FilePath: /fish_bot_ws/src/fishbot_app/fishbot_app/get_robot_pose.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener, Buffer
from tf_transformations import euler_from_quaternion


class TFListener(Node):
    def __init__(self):
        super().__init__('tf2_listener')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.tf_timer = self.create_timer(1, self.get_transform)
        self.get_logger().info('TF listener initialized')

    def get_transform(self):
        try:
            tf = self.tf_buffer.lookup_transform(
                'map', 'base_footprint', rclpy.time.Time(seconds=0), rclpy.time.Duration(seconds=1))
            transform = tf.transform
            rotation_euler = euler_from_quaternion([
                transform.rotation.x,
                transform.rotation.y,
                transform.rotation.z,
                transform.rotation.w
            ])
            self.get_logger().info(
                f'平移:{transform.translation},旋转四元数:{transform.rotation}:旋转欧拉角:{rotation_euler}')
        except Exception as e:
            self.get_logger().warn(f'不能够获取坐标变换，原因: {str(e)}')

def main():
    rclpy.init()
    node = TFListener()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

