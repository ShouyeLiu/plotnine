from __future__ import absolute_import, division, print_function

from ..utils.exceptions import GgplotError
from ..utils import alias
from .scale import scale_discrete, scale_continuous


def linetype_pal():
    linetypes = ['solid', 'dashed', 'dashdot', 'dotted']

    def func(n):
        l = list(linetypes)
        if n <= len(linetypes):
            return l[:n]
        else:
            return l + [None] * (n - len(linetypes))

    return func


class scale_linetype(scale_discrete):
    """
    Scale for line patterns

    Has the same arguments as :class:`~scale_discrete`
    """
    aesthetics = ['linetype']
    palette = staticmethod(linetype_pal())


class scale_linetype_continuous(scale_continuous):
    def __init__(self):
        raise GgplotError(
            "A continuous variable can not be mapped to linetype")


alias('scale_linetype_discrete', scale_linetype)