import tkinter as tk
import time, threading
from datetime import datetime, timedelta

# seconds=5
# lbl={'text':'0'}

# def updateEndTime():
#     endTime=datetime.now()+timedelta(seconds=seconds)
#     return endTime

# def startTimer(*args):
#     t=threading.Thread(target=runTimer,kwargs={'endTime':updateEndTime()},daemon=True)
#     t.start()

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self)
        self.master=master
        self.seconds=20
        self.lbl=tk.Label(text='OSC Tymer')
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')

        master.bind('x',self.quit)
        master.bind('g',self.startTimer)

    def updateEndTime(self):
        endTime=datetime.now()+timedelta(seconds=self.seconds)
        return endTime

    def startTimer(self,*args):
        self.runTimer(self.updateEndTime())

    def formatTimer(self,endTime):
        tmr=endTime-datetime.now()
        tmrSplit=str(tmr).split(':')
        return f'{tmrSplit[1]}:{tmrSplit[2][:2]}'

    def runTimer(self,endTime):
        while self.formatTimer(endTime)!='00:00':
            self.lbl['text']=self.formatTimer(endTime)
            time.sleep(.5)
        self.lbl['text']='00:00'
        
    def quit(self,*args):
        self.master.destroy()
        self.finish=True

root=tk.Tk()
app=App(root)

# def formatTimer(endTime):
#     tmr=endTime-datetime.now()
#     tmrSplit=str(tmr).split(':')
#     return f'{tmrSplit[1]}:{tmrSplit[2][:2]}'

# def runTimer(endTime=None):
#     while formatTimer(endTime)!='00:00':
#         lbl['text']=formatTimer(endTime)
#         app.lbl['text']=lbl['text']
#         print('updated clock...',lbl['text'])
#         time.sleep(1)
#         print('sleep for 1 sec...')
#     print('00:00')

# root.mainloop()

finished=False
while not finished:
    #...
    # osc_process()
    root.update_idletasks()
    root.update()
    #...
# osc_terminate()