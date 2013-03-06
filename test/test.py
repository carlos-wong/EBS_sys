#!/usr/bin/python
# -*- coding: UTF-8 –*-

import unittest
import sys
sys.path.append("../")
from ebs.orgmode.input import Parseinput

class testinput(unittest.TestCase):
    def setUp(self):
        print "setUp"
        self.parseinput = Parseinput()

    def tearDown(self):
        del(self.parseinput)
    def testinput(self):
        assert self.parseinput.get_input("./test_res/file.txt") == "./test_res/file.txt"
        assert self.parseinput.get_input("./test_rest/1231231") == ''
        assert self.parseinput.get_input("./test_rest") == ''
        

if __name__ == '__main__':
    unittest.main()
