# -*- coding: utf-8 -*-
import pkg_resources

from doctest_cmds import is_ok

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'
