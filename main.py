#!/usr/bin/python
import kivy
from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import (
    NumericProperty, StringProperty)
from kivy.event import EventDispatcher
import time
from osc4py3.as_allthreads import *
from osc4py3 import oscmethod as osm

kivy.require('1.11.0')
IP = '192.168.0.7'
PORT = 53000
osc_startup()
osc_udp_server(IP, PORT, 'OSCtimer')
# uncomment to go fullscreen
# Config.set('graphics','fullscreen','auto')

class OSC_Dispatcher(EventDispatcher):
    def __init__(self,**kwargs):
        super(OSC_Dispatcher,self).__init__(**kwargs)
        self.register_event_type('on_OSC')

    def on_OSC(self,*args):
        print('i am dispatched')
        for i in args:
            print(i)

'''
I need the osc_method to dispatch an on_OSC event to the bound callback functions
that will update the Label text. The issue is how to specify what is dispatching.

'''
x = OSC_Dispatcher()

def OSC_handler(addr, val):
    try:
        print(addr, val)
        #...
        x.dispatch('on_OSC', addr, val)
        
        #...
    except Exception as e:
        print(e)

osc_method('*',OSC_handler, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

class Timer(Widget):
    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)


    new_num = NumericProperty(0)
    tmrStr = StringProperty('00:00:00')

    # def updateEndTime(self):
    #     endTime=time.time()+self.seconds
    #     return endTime

    # def startTimer(self):
    #     self.runTimer(self.updateEndTime())

    # def runTimer(self,endTime):
    #     print('starting timer...')
    #     for i in range(self.seconds):
    #         tmr=time.gmtime(endTime-time.time())
    #         print(time.strftime('%H:%M:%S', tmr))

print('before TimerApp...')

class TimerApp(App):
    print('inside TimerApp before build()...')
    def build(self):
        return Timer()
        
print('after TimerApp...')

if __name__ == '__main__':
    TimerApp().run()

osc_terminate()
print('end...')