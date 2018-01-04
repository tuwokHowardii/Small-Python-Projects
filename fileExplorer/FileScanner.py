#created by tuwokHowardii for an assignment
import os
from os import path

class FileScanner:
    '''FileScanner will hold the details of whatever path the
    program is in or whatever path is passed as an arguement.
    '''
    def __init__(self,filepath=None):
        if filepath:
            self.path = filepath
            self.dir = path.dirname(r'%s'%self.path)
        else:
            self._realpath = self._getpath()
            self.path = self._realpath.replace('\\','/')
    def _getpath(self):
        pathname = path.abspath('')
        return pathname
    def dir(self):
        print(path.dirname(r'+%s'%self.path))
        for root, dirs, files in os.walk(self.path):
            for file in files:
                print(' -',file, '    ',end='')
                print(path.getsize(path.join(self.path,file)),'bytes')
            

__author__ = 'tuwokHowardii'
