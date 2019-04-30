from setuptools import setup, find_packages

setup(name='obstinate',
    version='0.1',
    description='Automaticaly replays a request when a connection error occurs',
    url='https://github.com/benjamindelmee/obstinate-requests',
    author='Benjamin Delmee',
    author_email='benjamindelmee@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    zip_safe=False
)