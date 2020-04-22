#!/usr/bin/python

from osc4py3.as_allthreads import *
from osc4py3 import oscmethod as osm
# import threading

def testOSC(add, val):
    print(add, val)

def quitOSC(*args):
	osc_terminate()
	sys.exit(1)

def startOSC(*args):
	print('you pressed start!')

IP='192.168.0.7'
PORT=53000
osc_startup()
osc_udp_server(IP,PORT,'testOSC')

osc_method('/transport/pause',quitOSC)
osc_method('/transport/start',startOSC)
osc_method('*',testOSC, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)