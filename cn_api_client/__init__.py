# -*- coding: utf-8 -*-
import pkg_resources

from .camara import Camara

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'


