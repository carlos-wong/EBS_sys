#!/usr/bin/python
# -*- coding: UTF-8 –*-

import unittest
import sys
sys.path.append("../")
from ebs.orgmode.input import Parseinput
from ebs.orgmode.readorg import Readorg

class testinput(unittest.TestCase):
    def setUp(self):
        # print "setUp"
        self.parseinput = Parseinput()

    def tearDown(self):
        del(self.parseinput)
    def testinput(self):
        assert self.parseinput.get_input("./test_res/file.txt") == "./test_res/file.txt"
        assert self.parseinput.get_input("./test_rest/1231231") == ''
        assert self.parseinput.get_input("./test_rest") == ''


        
class testorg2(unittest.TestCase):
    def setUp(self):
        self.org = Readorg()
        assert self.org.parsefile("./test_res/test1.org") == [0,2,7,11,16,39,52,56,58,61,66]
    def tearDown(self):
        del(self.org)
    def testnormal(self):
        assert self.org.readStep()[0] == 48
        assert self.org.readStep()[0] == 324
        assert self.org.readStep()[0] == 252
        assert self.org.readStep()[0] == 116
        assert self.org.readSteps(0)[0] == 48
        assert self.org.readSteps(3)[0] == 116
        assert self.org.readSteps(1)[0] == 324
        assert self.org.readSteps(2)[0] == 252
        assert self.org.readSteps(4)[0] == 1343
    def testgetclok(self):
        assert self.org.getRealClock(self.org.readSteps(4)[1]) == 509
        assert self.org.getRealClock(self.org.readSteps(9)[1]) == 6
    def testgetebs(self):
        assert self.org.getEbsTime(self.org.readSteps(4)[1]) == 1440
        assert self.org.getEbsTime(self.org.readSteps(3)[1]) == 90


class testorg1(unittest.TestCase):
    def setUp(self):
        self.org = Readorg()
        assert self.org.parsefile("./test_res/test.org") == [0, 1, 4, 6, 7, 8, 10, 15, 19, 24, 47, 60, 64, 66, 69, 74, 77, 83, 92, 95, 110, 112, 114, 119, 121, 135, 142, 144, 184, 186, 187, 194, 197, 200, 201, 203, 206, 209, 211, 254, 268, 270, 275, 280, 282, 284, 297, 299, 301, 303, 306, 308, 317, 325, 333, 334, 335, 337, 339, 341, 343, 345, 347, 350, 354, 355, 361, 362, 384, 390, 394, 397, 400]
        
    def tearDown(self):
        del(self.org)
        
    def test(self):
        assert self.org.readStep()[0] == 5
        assert self.org.readStep()[0] == 237
        assert self.org.readStep()[0] == 33
        assert self.org.readStep()[0] == 5
        assert self.org.readSteps(1)[0] == 237
        assert self.org.readSteps(0)[0] == 5
        assert self.org.readSteps(2)[0] == 33
        
    def testgetdata(self):
        self.org.getRealClock(self.org.readSteps(1)[1])

   
class testorg(unittest.TestCase):
    def setUp(self):

        pass
    def tearDown(self):
        pass
    def testorg(self):
        self.readorg = Readorg()
        assert self.readorg.ismark("*** casdcads") == 1
        assert self.readorg.ismark("* casdcdas") == 1
        assert self.readorg.ismark("** cadcads") == 1
        assert self.readorg.ismark("**** cadscsa") == 1
        assert self.readorg.ismark("casdcscasd") == 0
        assert self.readorg.ismark("      :@work:") == 0
        assert self.readorg.ismark("     CLOCK: [2013-01-29 Tue 15:26]--[2013-01-29 Tue 17:21] =>  1:55") == 0
        assert self.readorg.ismark("     可以判断msc_spl的数据。指定一个长度然后进行读取。应该指定第二阶") == 0
        del(self.readorg)

    def testparse(self):
        self.readorg = Readorg()
        assert self.readorg.parsefile("./test_res/test.org") == [0, 1, 4, 6, 7, 8, 10, 15, 19, 24, 47, 60, 64, 66, 69, 74, 77, 83, 92, 95, 110, 112, 114, 119, 121, 135, 142, 144, 184, 186, 187, 194, 197, 200, 201, 203, 206, 209, 211, 254, 268, 270, 275, 280, 282, 284, 297, 299, 301, 303, 306, 308, 317, 325, 333, 334, 335, 337, 339, 341, 343, 345, 347, 350, 354, 355, 361, 362, 384, 390, 394, 397, 400]
        del(self.readorg)
        self.readorg = Readorg()
        assert self.readorg.parsefile("./test_res/test1.org") == [0,2,7,11,16,39,52,56,58,61,66]
        del(self.readorg)
    def testreadstep(self):
        self.org = Readorg()
        assert self.org.parsefile("./test_res/test.org") == [0, 1, 4, 6, 7, 8, 10, 15, 19, 24, 47, 60, 64, 66, 69, 74, 77, 83, 92, 95, 110, 112, 114, 119, 121, 135, 142, 144, 184, 186, 187, 194, 197, 200, 201, 203, 206, 209, 211, 254, 268, 270, 275, 280, 282, 284, 297, 299, 301, 303, 306, 308, 317, 325, 333, 334, 335, 337, 339, 341, 343, 345, 347, 350, 354, 355, 361, 362, 384, 390, 394, 397, 400]

        assert self.org.readStep()[0] == 5
        assert self.org.readStep()[0] == 237
        assert self.org.readStep()[0] == 33
        assert self.org.readStep()[0] == 5
        assert self.org.readSteps(1)[0] == 237
        assert self.org.readSteps(0)[0] == 5
        assert self.org.readSteps(2)[0] == 33
        del(self.org)
        self.org = Readorg()
        assert self.org.parsefile("./test_res/test1.org") == [0,2,7,11,16,39,52,56,58,61,66]
        assert self.org.readStep()[0] == 48
        assert self.org.readStep()[0] == 324
        assert self.org.readStep()[0] == 252
        assert self.org.readStep()[0] == 116
        assert self.org.readSteps(0)[0] == 48
        assert self.org.readSteps(3)[0] == 116
        assert self.org.readSteps(1)[0] == 324
        assert self.org.readSteps(2)[0] == 252
        del(self.org)


if __name__ == '__main__':
    unittest.main()
