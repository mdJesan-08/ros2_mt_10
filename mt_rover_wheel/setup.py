from setuptools import find_packages, setup

package_name = 'mt_rover_wheel'

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
            'pub_joy_mav=mt_rover_wheel.joy_mavlink:main',

            'get_mav_joy=mt_rover_wheel.get_mavlink:main',
        ],
    },
)
