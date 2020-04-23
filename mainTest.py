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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

    tempStr = StringProperty('0000')

    def on_OSC(self, addr, val):
        print('on_OSC was dispatched...')

    def OSC_handler(self, addr, val): # OSC address and Value
        print('trying to handle...')
        try:
            self.dispatch('on_OSC', addr, val)
            self.tempStr = self.tempStr[1:]+str(int(val))
            print(self.tempStr)
            print('OSC handled...')
        except Exception as e:
            print(e)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TimerApp(App):

    def build(self):
        t = Timer()

        def cb(self, addr, val):
            print('cb():', self, addr, val)

        osc_method('*',t.OSC_handler, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)
        t.bind(on_OSC=cb)

        return t

if __name__ == '__main__':
    TimerApp().run()

osc_terminate()
print('end...')