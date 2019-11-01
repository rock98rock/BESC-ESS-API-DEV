from setuptools import setup, find_packages

setup(
    name='besc-ess-api',
    version='0.1dev',
    packages=find_packages(),
    license='MIT License',
    description='Send data to the ESS API',
    download_url='https://github.com/rock98rock/BESC-ESS-API-DEV/archive/0.1dev.tar.gz',
    install_requires=['query_string'],
    author='Clive Lim'
)
