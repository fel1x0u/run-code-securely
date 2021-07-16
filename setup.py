from setuptools import setup, find_packages
from os import path
from json import loads, dumps

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open(path.join(this_directory, 'requirements.json'), encoding='utf-8') as f:
    REQUIREMENTS = loads(f.read())


VERSION = '0.1.1'
DESCRIPTION = 'Package for running code with the Piston API.'

setup(
    name='run-code-securely',
    description='run-code-securely is a package to run python3 code with the PistonAPI.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    keywords=['python', 'code', 'requests', 'json', 'piston']

    )