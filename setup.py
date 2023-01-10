from setuptools import setup
import os
from glob import glob

package_name = 'py_pkg_template'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='todo@email.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "dummy_py_node = py_pkg_template.py_node_template:main",
            "dummy_publisher_py_node = py_pkg_template.py_publisher_template:main",
            "dummy_subscriber_py_node = py_pkg_template.py_subscriber_template:main",
            "dummy_server_py_node = py_pkg_template.py_service_server_template:main",
            "dummy_client_py_node = py_pkg_template.py_service_client_template:main",
        ],
    },
)
