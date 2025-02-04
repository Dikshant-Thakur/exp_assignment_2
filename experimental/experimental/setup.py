from setuptools import setup

package_name = 'experimental'  # Package name should be a string

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nathan Sprague',
    maintainer_email='nathan.r.sprague@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'exp2 = experimental.exp2:main',  # Entry point
        ],
    },
)

