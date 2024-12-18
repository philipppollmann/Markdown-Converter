"""

"""
from setuptools import setup, find_packages

setup(
    name='markdown_converter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'markitdown',
    ],
    entry_points={
        'console_scripts': [
            'mdc=markdown_converter.cli:main',
        ],
    },
)