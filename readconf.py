#!/usr/bin/python
import tempfile
from platform import system as systemos

ostype = systemos().lower()
tmpdir = tempfile.gettempdir()

def readconf():
    if ostype == 'windows':
        cfgfile = tmpdir + '\conf.ini'
        return cfgfile
    else:
        cfgfile = tmpdir+'/conf.ini'
        return cfgfile
		
if __name__ == "__main__":

	readconf()