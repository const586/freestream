#!/usr/bin/python2.7
import os
import sys
curdir = os.path.abspath(os.path.dirname(sys.argv[0]))
from freestream.Plugin.EngineConsole import start
apptype = 'freestream'
start(apptype, curdir)

