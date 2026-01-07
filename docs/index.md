# k3heap

[![Action-CI](https://github.com/pykit3/k3heap/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3heap/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3heap/badge/?version=stable)](https://k3heap.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3heap)](https://pypi.org/project/k3heap)

Binary min heap implemented with references. Each node maintains parent and child references for efficient sifting operations.

k3heap is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3heap
```

## Quick Start

```python
import k3heap

# Create a heap and push items
h = k3heap.RefHeap()
h.push(5)
h.push(2)
h.push(8)
h.push(1)

# Pop items in sorted order (min first)
print(h.pop())  # 1
print(h.pop())  # 2
print(h.pop())  # 5
print(h.pop())  # 8

# Initialize from iterable
h = k3heap.RefHeap([3, 1, 4, 1, 5])
print(h.pop_all())  # [1, 1, 3, 4, 5]

# Use with custom objects (must support < comparison)
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __lt__(self, other):
        return self.priority < other.priority

h = k3heap.RefHeap()
t1 = Task(3, "low")
t2 = Task(1, "high")
h.push(t1)
h.push(t2)
print(h.pop().name)  # "high"

# Update priority and re-sift
t1.priority = 0
h.sift(t1)  # Re-sort after priority change
```

## API Reference

::: k3heap

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
