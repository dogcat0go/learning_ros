'''
Author: LCOIT dogcat.let@gmail.com
Date: 2026-04-16 18:22:05
LastEditors: LCOIT dogcat.let@gmail.com
LastEditTime: 2026-04-23 00:16:07
FilePath: /fish_bot_ws/src/autopartol_robot/setup.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'autopartol_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name, 'config'), glob('config/*yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lcoit',
    maintainer_email='dogcat.let@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'patrol_node = autopartol_robot.partol_node:main',
            'speaker = autopartol_robot.speaker:main',
        ],
    },
)
