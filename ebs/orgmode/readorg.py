# -*- coding: UTF-8 –*-

import sys
import os
import linecache

class Readorg:
    def __init__(self):
        self.cur = 0
        self.mark = []
        self.step = 0
        # for self.line in self.fp:
        #     if(self.ismark(self.line)):
        #         self.mark.append(self.cur)
        #     self.cur += 1
        # return self.mark

    def readStep(self):
        # print "start to read step step is ",self.step,""
        self.stepreturn = ''
        if((self.mark[self.step+1] - self.mark[self.step]) == 1):
            self.stepreturn = "empty"
        else:
            for self.readline in range(self.mark[self.step],self.mark[self.step+1]-1):
                # print
                # linecache.getline(self.filename,self.readline+1)
                # print "read lien is :",self.readline 
                self.stepreturn += linecache.getline(self.filename,self.readline+2)
        self.step += 1
        
        # print "step is ",self.step,"length is ",len(self.stepreturn)
        return [len(self.stepreturn),self.stepreturn]

    def readSteps(self,step):
        self.stepreturn = ''
        if((self.mark[step+1] - self.mark[step]) == 1):
            self.stepreturn = "empty"
        else:
            for self.readline in range(self.mark[step],self.mark[step+1]-1):
                # print
                # linecache.getline(self.filename,self.readline+1)
                # print "read lien is :",self.readline 
                self.stepreturn += linecache.getline(self.filename,self.readline+2)
            
        # print "step is ",step,"length is ",len(self.stepreturn)
        return [len(self.stepreturn),self.stepreturn]
    
    def parsefile(self,filename):
        self.cur = 0
        self.filename = filename
        # print "start to parse file"
        # self.mark = []
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

            


            
