import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

VERSION = '0.1.0'

INSTALL_REQUIRES=[
    'requests',
    ]


TESTS_REQUIRE=('pytest', 'coverage')

if sys.version_info[:2] < (2, 6):
    raise RuntimeError('Requires Python 2.6 or later')

if sys.version_info[1] == 6:
    # NOTE: Starting Python 2.7, argparse is a built-in.
    INSTALL_REQUIRES.append('argparse')

# NOTE: To enable support for 'python setup.py test'
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='howfary.core',
    packages=find_packages(exclude=["tests"]),
    namespace_packages=['howfary'],
    version=VERSION,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    entry_points={'console_scripts': ['howfar = howfary.core.cli:howfar']},
    cmdclass={'test': PyTest},
)
