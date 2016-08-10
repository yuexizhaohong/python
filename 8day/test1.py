#!/usr/bin/env python


import os
import sys

#print sys.argv
#sys.exit(1)
for i in range(len(sys.argv)-1):
     arg = sys.argv[i+1]
     os.system('/home/chu/shell/test.sh' + " " + arg) 
