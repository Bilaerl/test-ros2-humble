from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='test_python',
            executable='talker',
            name='talker'
        ),
        Node(
            package='test_python',
            executable='listener',
            name='listener'
        ), 
    ])
