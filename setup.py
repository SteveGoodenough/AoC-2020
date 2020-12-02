from setuptools import setup, find_packages

setup(
    name="aoc",
    packages=find_packages(where='.'),
    include_package_data=True,
    package_dir={'': '.'}
)
