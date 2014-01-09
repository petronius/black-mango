"""
Basic setup file. Temporary.
"""

import setuptools

version = '0.0.0'

if __name__ == "__main__":

    ## This is being used mostly to track dependencies and automate testing. I
    ## don't ever anticipate releasing this project as open source, although we
    ## could at some point generalize it into a simpler framework that we do
    ## release.

    setuptools.setup(
        name = 'blackmango',
        version = '0.0.0',
        py_modules = [
            'blackmango',
            'blackmango_tests',
        ],
        install_requires = [
            'pyglet>=1.1.4',
        ],
        tests_require = [
            'mock>=1.0.1',
        ],
        test_suite = 'blackmango_tests.TestSuite',
    )
