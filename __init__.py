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

__version__ = "0.1.3"
__name__ = "k3heap"

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
