# -*- coding: utf-8 -*- vim:fileencoding=utf-8:

__version__ = '2.3.7'

__all__ = ['Cling', 'Error', 'Reactor']


class Error(Exception):
    """The module's generic exception"""


from cli import Cling
from reactor import Reactor
