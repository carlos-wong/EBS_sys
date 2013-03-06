# -*- coding: UTF-8 –*-

import sys
import os

class Readorg:
    def __init__(self):
        self.cur = 0
        self.mark = []
        # for self.line in self.fp:
        #     if(self.ismark(self.line)):
        #         self.mark.append(self.cur)
        #     self.cur += 1
        # return self.mark

    def readStep(self):
        pass

    def parsefile(self,filename):
        self.cur = 0
        print "start to parse file"
        self.mark = []
        self.fp = open(filename)
        for self.line in self.fp:
            # print self.line
            if(self.ismark(self.line)):
                self.mark.append(self.cur)
            self.cur += 1
        # print self.mark
        return self.mark
    def __del__(self):
        # self.fp.close()
        pass
    def ismark(self,data):
        i = 0
        for self.char in data:
            # print self.char
            if(self.char != '*'):
                # print "break"
                break
            i += 1
        # print i,self.char
        if i == 0:
            return 0
        if self.char != ' ':
            return 0
        else:
            return 1

            


            
