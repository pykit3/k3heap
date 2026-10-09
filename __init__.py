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


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3heap")
