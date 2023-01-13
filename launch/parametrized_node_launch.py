from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    parametrized_node = Node(
            package='py_pkg_template',
            executable='dummy_parametrized_py_node',
            name='dummy_parametrized_py',
            parameters=[
                {'timer_delta_ms': 1500},
                {'word': 'Dummy'}
            ]
        )

    return LaunchDescription([
        parametrized_node
    ])
