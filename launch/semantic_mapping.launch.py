from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='semantic_mapping_pkg',
            executable='sematic',
            name='sematic_mapping',
            namespace='robot1',
            output='screen',
        ),
    ])