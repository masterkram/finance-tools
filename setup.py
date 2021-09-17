from setuptools import setup
setup(
    name = 'finance-tools',
    version = '0.1.0',
    packages = ['fincli'],
    entry_points = {
        'console_scripts': [
            'fincli = fincli.__main__:main'
        ]
    })