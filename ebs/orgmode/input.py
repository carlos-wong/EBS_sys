# -*- coding: UTF-8 –*-

import sys
import os

class Parseinput:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def get_input(self,filename):
        if(os.path.isfile(filename)):
            return filename
        else:
            return ''
