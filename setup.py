from setuptools import setup, find_packages

setup(
    name='besc-ess-api',
    version='0.1dev',
    packages=find_packages(),
    license='MIT License',
    description='Send data to the ESS API',
    long_description=open('README.txt').read(),
    install_requires=['query_string'],
    author='Clive Lim'
)
