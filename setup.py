"""Distutils file for MPipe."""

from distutils.core import setup, Command
import subprocess
import inspect
import shutil
import os
import sys

class Clean2(Command):
    """A more thorough clean command."""
    description = 'clean everything generated by the build command'
    user_options = []
    def initialize_options(self): pass  # Must override.
    def finalize_options(self): pass  # Must override.
    def run(self):
        to_remove = ('build','dist','MANIFEST',)
        this_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        this_dir = os.path.normpath(this_dir)
        for entry in os.listdir(this_dir):
            if entry not in to_remove:
                continue
            entry = os.path.join(this_dir, entry)
            print('erasing {0}'.format(entry))
            if os.path.isfile(entry):
                os.remove(entry)
            elif os.path.isdir(entry):
                shutil.rmtree(entry)

class Test(Command):
    """A custom test command."""
    description = 'run custom test suite'
    user_options = []
    def initialize_options(self): pass  # Must override.
    def finalize_options(self): pass  # Must override.
    def run(self):
        this_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        this_dir = os.path.normpath(this_dir)
        args = os.path.join(this_dir, 'test', 'test.py')
        command = '{0} {1}'.format(sys.executable, args)
        print(command)
        subprocess.call(command, shell=True)

from src.mpipe import __version__ as version

setup(
    name         = 'mpipe',
    version      = version,
    description  = 'A multiprocess pipeline software framework.',
    url          = 'http://vmlaker.github.io/mpipe',
    author       = 'Velimir Mlaker',
    author_email = 'velimir.mlaker@gmail.com',
    license      = 'MIT',
    long_description = open('README.rst').read(),
    package_dir  = {'' : 'src'},
    py_modules   = ['mpipe'],
    cmdclass     = { 'clean2' : Clean2, 'test' : Test, },
    classifiers  = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
