from setuptools import find_packages, setup

package_name = 'semantic_mapping_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/semantic_mapping.launch.py']),
        ('share/' + package_name + '/web', ['web/multi_robot_dashboard.html']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jay',
    maintainer_email='jaygajjar890@gmail.com',
    description='YOLO + LiDAR semantic object mapping and navigation for TurtleBot3',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sematic = semantic_mapping_pkg.sematic_object_localization:main',
        ],
    },
)