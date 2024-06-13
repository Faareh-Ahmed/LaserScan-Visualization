from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='urg_node',
            executable='urg_node_driver',
            name='urg_node',
            output='screen',
            parameters=[{
                'ip_address': '192.168.0.10',  # Replace with your LiDAR's IP address
                'port': 10940,                 # Replace with your LiDAR's port number (default is usually 10940)
                # 'angle_max': 270,
                # 'angle_min': 0,
                'publish_intensity': False,
                'publish_multiecho': False,
                'use_sim_time': False,
                'frame_id': 'laser',
                'depth': 10
            }],
            remappings=[],
        ),
    ])
