#!/usr/bin/python

from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import (
    NumericProperty, ObjectProperty)
from kivy.event import EventDispatcher
import time

# Config.set('graphics','fullscreen','auto')
print('before TimerApp')
# seconds=5

class OSC_Dispatcher(EventDispatcher):
    def __init__(self,**kwargs):
        self.register_event_type('on_test')
        super(OSC_Dispatcher,self).__init__(**kwargs)

    def do_someting(self,value):
        self.dispatch('on_test',value)

    def on_test(self,*args):
        print('i am dispatches',args)

class Timer(Widget):
    seconds=NumericProperty(5)
    timer=ObjectProperty(None)

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
    
    print('Timer defined...')

print('???')

class TimerApp(App):
    def build(self):
        Timer().startTimer()
        return Timer()

print('beofore .run()')
        
if __name__ == '__main__':
    TimerApp().run()

print('end...')

'''
I need to update the Label text with a Clock object every second until the timer 
reaches zero, then ClockEvent.cancle() the schedule_interval()


'''