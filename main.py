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
from osc4py3.as_allthreads import * # the allthreads option eliminates the need to declare osc_process() in the event loop
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
#~~works~~
class OSC_Dispatcher(EventDispatcher):
    def __init__(self,**kwargs):
        super(OSC_Dispatcher,self).__init__(**kwargs)
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
'''
this works, but i think it would be best to move the event dispatcher inside
of the Timer widget so that the timerStr is unique to that timer. Will this 
be necessary with multiple timers?
'''
# osc = OSC_Dispatcher()

# def OSC_handler(addr, val):
#     osc.dispatch('on_OSC', addr, val)

# osc_method('*',OSC_handler, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Timer(Widget):
    
    osc = OSC_Dispatcher()

    def cb(self, addr, val):
        print('cb():', self, addr, val)

    # def updateTimer(self, addr, val):
    #     if addr == '/numpad':
    #         try:
    #         # update tempStr
    #             self.tempStr = self.tempStr[1:]+str(int(val))
    #             print(self.tempStr)
    #         except Exception as e:
    #             print(e)
    #     elif addr == '/enter':
    #         # set timer text to tempStr
    #         print('enter...')
    #     elif addr == '/clear':
    #         print('clear')
    #     elif addr == '/start':
    #         print('start...')
    #     elif addr == '/pause':
    #         print('pause...')

    osc_method('*',osc.OSC_handler, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)
    #~~works~~

    # def updateEndTime(self):
    #     endTime=time.time()+self.seconds
    #     return endTime

    # def startTimer(self):
    #     self.runTimer(self.updateEndTime())

    # def runTimer(self,endTime):
    #     print('starting timer...')
    #     for i in range(self.seconds): # need to define seconds        
    #         tmr=time.gmtime(endTime-time.time())
    #         print(time.strftime('%H:%M:%S', tmr))
    osc.bind(on_OSC=cb)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TimerApp(App):
    # osc_method('*',OSC_handler, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)
    def build(self):
        return Timer()

if __name__ == '__main__':
    TimerApp().run()

osc_terminate()
print('end...')