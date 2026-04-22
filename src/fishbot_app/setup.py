'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-14 05:23:21
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-16 03:18:30
FilePath: /fish_bot_ws/src/fishbot_app/setup.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""Setup script for the fishbot_app package."""
from setuptools import find_packages, setup

package_name = 'fishbot_app'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lcoit',
    maintainer_email='dogcat.let@gmail.com',
    description='Fishbot application nodes (e.g. Nav2 initial pose).',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'init_robot_pose = fishbot_app.init_robot_pose:main',
            'get_robot_pose = fishbot_app.get_robot_pose:main',
            'nav_to_pose = fishbot_app.nav_to_pose:main',
            'waypoints_follow = fishbot_app.waypoints_follow:main',
        ],
    },
)
