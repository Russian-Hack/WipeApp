from setuptools import setup, find_packages

setup(
    name='WipeApp',
    version='1.0',
    packages=find_packages(),
    scripts=['your_script.py'],  # list all scripts to be included
    install_requires=[  # list dependencies here
        'psutil',

    ],
)