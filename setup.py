import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'usb_cam_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=[f'{package_name}'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lunan',
    maintainer_email='arlunan@ieee.org',
    description='Neato Turtle Extras - turtlebot & usb_cam bringup',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'usb_cam = {package_name}.launch:main',
        ],
    },
)