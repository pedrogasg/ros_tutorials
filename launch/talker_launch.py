# generate launch description to launch a node with the demo_nodes_cpp package
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='talker',
            name='talker'
        )
    ])
