"""
In this module RefHeap is a binary min heap implemented with reference: a parent has two references to two children and a child has a parent reference to its parent.

RefHeap is not thread safe::

    import k3heap

    h = k3heap.RefHeap()

    x = []
    h.push(x)
    h.push(x)  # ValueError
    h.push([]) # OK
"""

from importlib.metadata import version

__version__ = version("k3heap")

from .refheap import (
    Duplicate,
    Empty,
    NotFound,
    RefHeap,
    index_level,
)

__all__ = [
    "Duplicate",
    "Empty",
    "NotFound",
    "RefHeap",
    "index_level",
]
