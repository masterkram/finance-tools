from setuptools import setup
setup(
    name = 'finance-tools',
    version = '0.1.0',
    packages = ['finance-cli'],
    entry_points = {
        'console_scripts': [
            'finance-cli = finance-cli.__main__:main'
        ]
    })