#!/usr/bin/python
import kivy
from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import (
    NumericProperty, StringProperty, ObjectProperty)
from kivy.event import EventDispatcher
import time
# the allthreads option eliminates the need to declare osc_process() in the event loop
from osc4py3.as_allthreads import *
from osc4py3 import oscmethod as osm

kivy.require('1.11.1')
IP = '192.168.0.7'
PORT = 53000
osc_startup()
osc_udp_server(IP, PORT, 'OSCtimer')
# uncomment to go fullscreen
# Config.set('graphics','fullscreen','auto')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Timer(Widget):
    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)
        self.register_event_type('on_OSC')

    # place to hold input from OSC as MMSS
    tempStr = StringProperty('0000')
    # seconds left on timer
    seconds = NumericProperty(10)
    tmrStr = StringProperty('00:00')
    def updateEndTime(self):
        endTime=time.time()+self.seconds
        return endTime

    def on_tempStr(self, inst, val):
        # update seconds when tempStr changes
        self.seconds = int(self.tempStr[2:]) + (int(self.tempStr[:2])*60)
        print('seconds:', self.seconds)
        # format seconds into string to display
        tmr = time.gmtime(self.updateEndTime()-time.time()+1)
        print('tmr:',tmr)
        self.tmrStr = time.strftime('%M:%S', tmr)
        print('tmrStr:',self.tmrStr)

    def on_OSC(self, addr, val):
        pass
    
    # shift tempStr left and append val to right
    def OSC_handler(self, addr, val): # OSC address and Value
        try:
            self.dispatch('on_OSC', addr, val)
            self.tempStr = self.tempStr[1:]+str(int(val))
            print('new tempStr:',self.tempStr)
        except Exception as e:
            print(e)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TimerApp(App):
    def build(self):
        t = Timer()

        def cb(self, addr, val):
            # print('cb():', self, addr, val)
            pass

        osc_method('*',t.OSC_handler, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)
        t.bind(on_OSC=cb)

        return t

if __name__ == '__main__':
    TimerApp().run()

osc_terminate()
print('end...')