from __future__ import absolute_import, division, print_function

from ..utils.doctools import document
from .geom_bar import geom_bar


@document
class geom_col(geom_bar):
    """
    Bar plot with base on the x-axis

    This is an alternate version of :class:`geom_bar` that maps
    the height of bars to an existing variable in your data. If
    you want the height of the bar to represent a count of cases,
    use :class:`geom_bar`.

    {documentation}
    """
    REQUIRED_AES = {'x', 'y'}
    DEFAULT_PARAMS = {'stat': 'identity', 'position': 'stack',
                      'width': None}
