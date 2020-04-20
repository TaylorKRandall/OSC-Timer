#!/usr/bin/python

from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty)
import time

# Config.set('graphics','fullscreen','auto')
print('before TimerApp')

seconds=10

class Timer(Widget):
    # seconds=NumericProperty(20)
    timer=ObjectProperty('00:00:00')

    def updateEndTime(self):
        endTime=time.time()+seconds
        return endTime

    def startTimer(self):
        self.runTimer(self.updateEndTime())

    def runTimer(self,endTime):
        print('starting timer...')
        for i in range(seconds):
            tmr=time.gmtime(endTime-time.time())
            print(time.strftime('%H:%M:%S', tmr))
            time.sleep(1)
    
class TimerApp(App):
    def build(self):
        return Timer()

print('beofore .run()')
        
if __name__ == '__main__':
    TimerApp().run()

print('end...')