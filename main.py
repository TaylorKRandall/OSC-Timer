#!/usr/bin/python
import kivy
from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.event import EventDispatcher
import time
# the allthreads option eliminates the need to declare osc_process() in the event loop
from osc4py3.as_allthreads import *
from osc4py3 import oscmethod as osm
from functools import partial

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
    def on_OSC(self, val):
        pass

    # place to hold input from OSC as MMSS
    tempStr = StringProperty('0000')
    # referenced by Label
    tmrStr = StringProperty('00:00')
    # seconds left on timer
    seconds = 0
    # store end time so startTimer() can reference without resetting
    endTime = time.time()+seconds

    isPaused = True

    def updateEndTime(self):
        self.endTime=time.time()+self.seconds
        return self.endTime

    def on_tempStr(self, inst, val):
        # update seconds when tempStr changes
        self.seconds = int(self.tempStr[2:]) + (int(self.tempStr[:2])*60)
        # format seconds into string to display
        tmr = time.gmtime(self.updateEndTime()-time.time()+1)
        self.tmrStr = time.strftime('%M:%S', tmr)
    
    # shift tempStr left and append val to right
    def oscNumpadHandler(self, val): # OSC Value
        # self.dispatch('on_OSC', val)
        if self.isPaused == True:
            self.tempStr = self.tempStr[1:]+str(int(val))
        else:
            pass
    # does nothing for now
    def oscEnterHandler(self, val):
        pass

    def oscClearHandler(self, val):
        self.tempStr = '0000'

    def oscStartHandler(self, val):
        self.isPaused = False
        print('starting timer...')
        self.updateEndTime()
        Clock.schedule_interval(self.runTimer, 1/4.)

    def runTimer(self, dt):
        tmr = time.gmtime(self.endTime-time.time()+1)
        # check if the time has run out
        if tmr[4] + tmr[5] != 0 and self.isPaused == False:
            self.tmrStr = time.strftime('%M:%S', tmr)
        elif tmr[4] + tmr[5] != 0 and self.isPaused == True:
            return False
        else:
            # update one last time, reset tempStr, and unshedule Clock
            print('runTimer() returning false...')
            self.tmrStr = time.strftime('%M:%S', tmr)
            self.tempStr = '0000'
            return False

    def oscPauseHandler(self, val):
        # pause and set seconds to time remaining
        self.isPaused = True
        tmr = time.gmtime(self.endTime-time.time()+1)
        self.seconds = (tmr[4]*60)+tmr[5]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TimerApp(App):
    def build(self):
        t = Timer()

        def cb(self, val):
            # print('cb():', self, val)
            pass

        osc_method('/numpad', t.oscNumpadHandler)
        osc_method('/enter', t.oscEnterHandler)
        osc_method('/clear', t.oscClearHandler)
        osc_method('/start', t.oscStartHandler)
        osc_method('/pause', t.oscPauseHandler)
        t.bind(on_OSC=cb)

        return t

if __name__ == '__main__':
    TimerApp().run()

osc_terminate()
print('end...')