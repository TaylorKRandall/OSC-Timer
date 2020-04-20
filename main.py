#!/usr/bin/python

from kivy.app import App 
from kivy.clock import Clock 
from kivy.uix.label import Label
from kivy.config import Config
import time
from datetime import datetime, timedelta

# Config.set('graphics','fullscreen','auto')
seconds=20

class TimerApp(App):
    def build(self):
        timer=Label(text='OSC Tymer', font_size=100)

    def updateEndTime(self):
        endTime=datetime.now()+timedelta(seconds=seconds)
        return endTime

    # def startTimer(self,*args):
    #     self.runTimer(self.updateEndTime())

    # def formatTimer(self,endTime):
    #     tmr=endTime-datetime.now()
    #     tmrSplit=str(tmr).split(':')
    #     return f'{tmrSplit[1]}:{tmrSplit[2][:2]}'

    # def runTimer(self,endTime):
    #     while self.formatTimer(endTime)!='00:00':
    #     	pass
            # timer['text']=self.formatTimer(endTime)
            # time.sleep(1)

        return timer
        
if __name__ == '__main__':
    TimerApp().run()