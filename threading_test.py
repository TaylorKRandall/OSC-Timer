import threading
import tkinter as tk
import time
from datetime import datetime, timedelta

seconds=5
# endTime=datetime.now()+timedelta(seconds=seconds)
lbl={'text':'0'}

def updateEndTime():
    endTime=datetime.now()+timedelta(seconds=seconds)
    return endTime

def startTimer(*args):
    t=threading.Thread(target=runTimer,kwargs={'endTime':updateEndTime()},daemon=True)
    t.start()

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self)
        self.master=master
        self.lbl=tk.Label(text='OSC Tymer')
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')

        master.bind('x',self.quit)
        master.bind('g',startTimer)
        
    def quit(self,*args):
        self.master.destroy()
        self.finish=True

root=tk.Tk()
app=App(root)

def formatTimer(endTime):
    tmr=endTime-datetime.now()
    tmrSplit=str(tmr).split(':')
    return f'{tmrSplit[1]}:{tmrSplit[2][:2]}'

def runTimer(endTime=None):
    while formatTimer(endTime)!='00:00':
        lbl['text']=formatTimer(endTime)
        print('updated clock...',lbl['text'])
        time.sleep(1)
        print('sleep for 1 sec...')
    print('00:00')

# startTimer()

finished=False
while not finished:
    #...
    # osc_process()
    root.update_idletasks()
    root.update()
    #...
# osc_terminate()