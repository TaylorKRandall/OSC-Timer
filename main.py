#!/usr/bin/python

from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import (
    NumericProperty, ObjectProperty)
from kivy.event import EventDispatcher
import time
from osc4py3.as_allthreads import *
from osc4py3 import oscmethod as osm

#upcomment to go fullscreen
# Config.set('graphics','fullscreen','auto')
print('before TimerApp')
# IP='192.168.0.7'
# PORT=53000
# osc_startup()
# osc_udp_server(IP,PORT,'OSCtimer')

# class OSC_Dispatcher(EventDispatcher):
#     def __init__(self,**kwargs):
#         self.register_event_type('on_test')
#         super(OSC_Dispatcher,self).__init__(**kwargs)

#         osc_method('/transport/start',self.do_someting)

#     def do_someting(self,value):
#         self.dispatch('on_test',value)

#     def on_test(self,*args):
#         print('i am dispatches',args)

class Timer(Widget):
    seconds=NumericProperty(5)

    def updateEndTime(self):
        endTime=time.time()+self.seconds
        return endTime

    def startTimer(self):
        self.runTimer(self.updateEndTime())

    def runTimer(self,endTime):
        print('starting timer...')
        for i in range(self.seconds):
            tmr=time.gmtime(endTime-time.time())
            print(time.strftime('%H:%M:%S', tmr))

class TimerApp(App):
    def build(self):
        IP='192.168.0.7'
        PORT=53000
        osc_startup()
        osc_udp_server(IP,PORT,'OSCtimer')
        
        def testOSC(*args):
            for i in args:
                print(i)

        osc_method('/transport/start',testOSC)

        return Timer()
        
if __name__ == '__main__':
    TimerApp().run()

osc_terminate()
print('end...')

'''
I need to update the Label text with a Clock object every second until the timer 
reaches zero, then ClockEvent.cancle() the schedule_interval()


'''