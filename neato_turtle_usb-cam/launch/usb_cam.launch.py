import argparse
import os
import sys

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    parser = argparse.ArgumentParser(description='usb_cam launch')
    parser.add_argument('-n', '--node-name', dest='node_name', type=str,
                        help='name for device', default='usb_cam')

    args, unknown = parser.parse_known_args(sys.argv[4:])

    usb_cam_dir = get_package_share_directory('usb_cam'),
        
    # get path to params file
    params_path = os.path.join(
        usb_cam_dir,
        'config',
        'params10.yaml'
    )
        
    node_name = args.node.name

    print(params_path)
    ld.add_action(Node(
        package = 'usb_cam',
        name = 'node_name',
        executable = 'usb_cam_node_exe',
        parameters = [params_path]
    )) 
    
    return ld
