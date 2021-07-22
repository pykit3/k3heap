import doctest

import k3heap


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(k3heap))
    return tests
