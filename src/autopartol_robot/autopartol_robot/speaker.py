'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-22 08:09:00
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-22 08:09:52
FilePath: /fish_bot_ws/src/autopartol_robot/autopartol_robot/speaker.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import rclpy
from rclpy.node import Node
from autopartol_interfaces.srv import SpeachText
import espeakng

class Speaker(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.speech_service = self.create_service(
            SpeachText, 'speech_text', self.speak_text_callback)
        self.speaker = espeakng.Speaker()
        self.speaker.voice = 'zh'

    def speak_text_callback(self, request, response):
        self.get_logger().info('正在朗读 %s' % request.text)
        self.speaker.say(request.text)
        self.speaker.wait()
        response.result = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = Speaker('speaker')
    rclpy.spin(node)
    rclpy.shutdown()