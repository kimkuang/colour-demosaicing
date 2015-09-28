#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Colour - Demosaicing
====================

CFA (Colour Filter Array) Demosaicing algorithms for *Python*.

Subpackages
-----------
-   bayer: *Bayer* CFA mosaicing and demosaicing computations.
"""

from __future__ import absolute_import

from .bayer import *  # noqa
from . import bayer  # noqa

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = []
__all__ += bayer.__all__