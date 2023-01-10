from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    publisher_node = Node(
            package='py_pkg_template',
            executable='dummy_publisher_py_node',
            name='dummy_publisher_py'
        )

    subscriber_node = Node(
            package='py_pkg_template',
            executable='dummy_subscriber_py_node',
            name='dummy_subscriber_py',
            output='screen'
        )

    return LaunchDescription([
        publisher_node,
        subscriber_node
    ])
