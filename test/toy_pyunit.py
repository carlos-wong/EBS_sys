#!/usr/bin/python
# -*- coding: UTF-8 –*-

import unittest
import sys
sys.path.append("../")
from widget import Widget

class justest(unittest.TestCase):
    def setUp(self):
        print "setUp"
        self.widget = Widget("the widget")
    def tearDown(self):
        del(self.widget)
    def Testinit(self):
        assert self.widget.size() == (50,50), 'incorrect default size'
        assert self.widget.resize(10,10) == (10,10), 'incorrect when set 10 10'
    def testresize(self):
        assert self.widget.resize(123,123) == (123,123) , 'incrrect resize'

if __name__ == '__main__':
    unittest.main()
