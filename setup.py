try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.1.0'

setup(
    name='pynv',
    version='0.1.0',
    author='Anton Burnashev & Luke Chang',
    author_email='luke.j.chang@dartmouth.edu',
    url='https://github.com/ljchang/pynv',
    packages=['pynv'],
    license='MIT',
    install_requires=['requests>=2.10.0'],
    description='A Python library for interfacing with http://neurovault.org upload API',
    keywords=['neuroimaging', 'neurovault'],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ]
)
