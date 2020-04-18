#!/usr/bin/python

import time
from datetime import datetime, timedelta
import tkinter as tk
import tkinter.font
from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm
import threading

class App(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self)
		self.master=master
		self.lblTxt='OSC tymer' # Not used anymore
		self.lblFG='white'
		self.lblBG='black'
		self.seconds=45297
		self.endTime=datetime.now()+timedelta(seconds=self.seconds)
		self.timeStr=self.formatTimer(self.updateEndTime())
		self.lbl=tk.Label(text=self.timeStr,fg=self.lblFG,bg=self.lblBG)
		self.lbl.place(relx=0.5, rely=0.5, anchor='center')
		self.IP='192.168.0.7'
		self.PORT=53000

		osc_startup()
		osc_udp_server(self.IP,self.PORT,'OSCtimer')

		master.bind('x',self.quit)
		master.attributes('-fullscreen',True)
		master['bg']='black'

		osc_method('/timer/*',self.addTime)
		osc_method('/start/*',self.startTimer)

	def updateEndTime(self):
		self.endTime=datetime.now()+timedelta(seconds=self.seconds)
		return self.endTime

	def updateLbl(self):
		self.lbl['text']=self.formatTimer(self.endTime)
		return self.lbl

	def formatTimer(self,endTime):
		tmr=endTime-datetime.now()
		tmrSplit=str(tmr).split(':')
		return f'{tmrSplit[0]}:{tmrSplit[1]}:{tmrSplit[2][:2]}'
		# '[H]H:MM:S[S]'

	def addTime(self,*args):
		for i in args:
			self.seconds+=i
			updateEndTime()
			updateLbl()
			print('exiting handler...')

	def startTimer(self,*args):
		for i in args:
			updateEndTime()
			self.t=threading.Thread(target=self.runTimer,kwargs={'endTime':self.endTime},daemon=True)
			self.t.start()

	def runTimer(self,endTime=None):
		if self.seconds>0:
			while self.seconds>0:
				self.updateLbl()
				time.sleep(1)
		else:
			self.lbl['text']='00:00:00'

	def quit(self,*args):
		self.master.destroy()
		self.finished=True

root=tk.Tk()
app=App(root)

finished=False
while not finished:
	#...
	osc_process()

	root.update_idletasks()
	root.update()
	#...
osc_terminate()

# except Exception as e: