from setuptools import find_packages, setup

package_name = 'arc_workshop'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ARC',
    maintainer_email='nikolaisemin01@gmail.com',
    description='ARC ROS2 Workshop Python nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cmd_vel_reader = arc_workshop.cmd_vel_reader:main',
            'scan_direction_reader = arc_workshop.scan_direction_reader:main',
            'stop_on_obstacle = arc_workshop.stop_on_obstacle:main',
        ],
    },
)
