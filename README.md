# k3heap

[![Action-CI](https://github.com/pykit3/k3heap/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3heap/actions/workflows/python-package.yml)
[![Build Status](https://travis-ci.com/pykit3/k3heap.svg?branch=master)](https://travis-ci.com/pykit3/k3heap)
[![Documentation Status](https://readthedocs.org/projects/k3heap/badge/?version=stable)](https://k3heap.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3heap)](https://pypi.org/project/k3heap)

k3heap is a binary min heap implemented with reference

k3heap is a component of [pykit3] project: a python3 toolkit set.


In this module RefHeap is a binary min heap implemented with reference: a parent has two references to two children and a child has a parent reference to its parent.

RefHeap is not thread safe::

    import k3heap

    h = k3heap.RefHeap()

    x = []
    h.push(x)
    h.push(x)  # ValueError
    h.push([]) # OK



# Install

```
pip install k3heap
```

# Synopsis

```python

import k3heap

h = k3heap.RefHeap([5, 1, 4, 2, 3])

while h.size > 0:
    print(h.pop())

```

#   Author

Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>

#   Copyright and License

The MIT License (MIT)

Copyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>


[pykit3]: https://github.com/pykit3