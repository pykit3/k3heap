# DO NOT EDIT!!! built with `python _building/build_setup.py`
import setuptools
setuptools.setup(
    name="k3heap",
    packages=["k3heap"],
    version="0.1.5",
    license='MIT',
    description='k3heap is a binary min heap implemented with reference',
    long_description='# k3heap\n\n[![Action-CI](https://github.com/pykit3/k3heap/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3heap/actions/workflows/python-package.yml)\n[![Build Status](https://travis-ci.com/pykit3/k3heap.svg?branch=master)](https://travis-ci.com/pykit3/k3heap)\n[![Documentation Status](https://readthedocs.org/projects/k3heap/badge/?version=stable)](https://k3heap.readthedocs.io/en/stable/?badge=stable)\n[![Package](https://img.shields.io/pypi/pyversions/k3heap)](https://pypi.org/project/k3heap)\n\nk3heap is a binary min heap implemented with reference\n\nk3heap is a component of [pykit3] project: a python3 toolkit set.\n\n\nIn this module RefHeap is a binary min heap implemented with reference: a parent has two references to two children and a child has a parent reference to its parent.\n\nRefHeap is not thread safe::\n\n    import k3heap\n\n    h = k3heap.RefHeap()\n\n    x = []\n    h.push(x)\n    h.push(x)  # ValueError\n    h.push([]) # OK\n\n\n\n# Install\n\n```\npip install k3heap\n```\n\n# Synopsis\n\n```python\n\nimport k3heap\n\nh = k3heap.RefHeap([5, 1, 4, 2, 3])\n\nwhile h.size > 0:\n    print(h.pop())\n\n```\n\n#   Author\n\nZhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n#   Copyright and License\n\nThe MIT License (MIT)\n\nCopyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n\n[pykit3]: https://github.com/pykit3',
    long_description_content_type="text/markdown",
    author='Zhang Yanpo',
    author_email='drdr.xp@gmail.com',
    url='https://github.com/pykit3/k3heap',
    keywords=['python', 'heap'],
    python_requires='>=3.0',

    install_requires=['semantic_version~=2.8.5', 'jinja2~=3.0.1', 'PyYAML~=5.4.1', 'sphinx~=3.3.1', 'k3ut~=0.1.15'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ] + ['Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: Implementation :: PyPy'],
)
