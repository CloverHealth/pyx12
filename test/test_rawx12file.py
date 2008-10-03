#! /usr/bin/env /usr/local/bin/python

import unittest
import sys
#import StringIO
import pdb
import tempfile

import pyx12.error_handler
#from error_handler import ErrorErrhNull
from pyx12.errors import *
import pyx12.x12file
from pyx12.tests.x12file import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Delimiters))
    suite.addTest(unittest.makeSuite(ISA_header))
    #suite.addTest(unittest.makeSuite(Formatting))
    if sys.platform != 'win32':
        suite.addTest(unittest.makeSuite(FileString))
    return suite

try:
    import psyco
    psyco.full()
except ImportError:
    pass
unittest.TextTestRunner(verbosity=2).run(suite())

