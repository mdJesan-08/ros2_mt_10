from setuptools import find_packages, setup

package_name = 'mt_rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hasi',
    maintainer_email='hasi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = mt_rover.my_first_node:main",
            "move_turtle = mt_rover.drawCircle:main",
            "get_pose = mt_rover.poseSubscriber:main",
            "get_joy = mt_rover.joylistener:main"
        ],
    },
)
