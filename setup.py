from setuptools import setup, find_packages

setup(
    name="markdown_converter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "markitdown",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "project-name=markdown_converter.cli:main",
        ],
    },
)