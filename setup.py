from setuptools import setup, find_packages

setup(name='sketches',
    version='0.1',
    description='HyperLogLog and other probabilistic data structures for mining in data streams',
    author='Pavel Kalaidin',
    author_email='hello@perapera.ru',
    url='https://github.com/kalaidin/sketches',
    packages=find_packages(),
    install_requires=["numpy"])