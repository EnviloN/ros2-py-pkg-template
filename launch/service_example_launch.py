from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    client_node = Node(
            package='py_pkg_template',
            executable='dummy_client_py_node',
            name='dummy_client_py'
        )

    server_node = Node(
            package='py_pkg_template',
            executable='dummy_server_py_node',
            name='dummy_server_py'
        )

    return LaunchDescription([
        client_node,
        server_node
    ])
