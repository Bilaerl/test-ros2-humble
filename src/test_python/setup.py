import os
from glob import glob
from setuptools import setup

package_name = 'test_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bilal Babale',
    maintainer_email='bilalbabale@gmail.com',
    description='Test snap for ros2 Humble',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = test_python.talker:main',
            'listener = test_python.listener:main',
        ],
    },
)
