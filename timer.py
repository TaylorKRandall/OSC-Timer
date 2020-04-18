#!/usr/bin/python

import time
from datetime import datetime, timedelta
import tkinter as tk
import tkinter.font
from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

class App(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self)
		self.master=master
		self.lblTxt='OSC tymer'
		self.lblFG='white'
		self.lblBG='black'
		self.seconds=48690
		self.endTime=datetime.now()+timedelta(seconds=self.seconds)
		self.timeStr=self.formatTimer(self.endTime)
		self.lbl=tk.Label(text=self.timeStr,fg=self.lblFG,bg=self.lblBG)
		self.lbl.place(relx=0.5, rely=0.5, anchor='center')
		self.IP='192.168.0.7'
		self.PORT=53000

		osc_startup()
		osc_udp_server(self.IP,self.PORT,'OSCtimer')

		master.bind('x',self.quit)
		master.attributes('-fullscreen',True)
		master['bg']='black'

		osc_method('/timer/*',self.oscHandler)

	def formatTimer(self,endTime):
		tmr=endTime-datetime.now()
		tmrSplit=str(tmr).split(':')
		return f'{tmrSplit[0]}:{tmrSplit[1]}:{tmrSplit[2][:2]}'
		# '[H]H:MM:S[S]'

	def oscHandler(self,*args):
	# will receive message data unpacked in s,x,y
		for i in args:
			self.seconds+=i
			# strucTime=time.gmtime(self.seconds)
			# self.timeStr=time.strftime('%H:%M:%S',strucTime)
			# self.lbl['text']=self.timeStr
			print('exiting handler...')

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