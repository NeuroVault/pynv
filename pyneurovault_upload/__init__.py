"""
    pyneurovault_upload
    ~~~~~~~~~~~~~~~~~~~

    A client for interfacing with http://neurovault.org API


    :copyright: (c) 2016 by Luke Chang.
    :license: MIT, see LICENSE for more details.
"""

API_BASE_URL = 'http://neurovault.org/api/'

from client import Client

__all__ = ['Client']

__author__ = ['Luke Chang', 'Anton Burnashev']
__license__ = 'MIT'
