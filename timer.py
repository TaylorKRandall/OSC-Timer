#!/usr/bin/python

import tkinter as tk
import tkinter.font
from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

class App(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self)
		self.master=master
		self.lastClicked=None
		self.lblFG='white'
		self.lblBG='black'
		self.lbl=tk.Label(text=self.lastClicked,fg=self.lblFG,bg=self.lblBG)
		self.lbl.place(relx=0.5, rely=0.5, anchor='center')
		self.IP='192.168.0.7'
		self.PORT=53000

		osc_startup()
		osc_udp_server(self.IP,self.PORT,'OSCtimer')

		master.bind('x',self.quit)
		master.attributes('-fullscreen',True,'-titlepath','timer.py')
		master['bg']='black'

		osc_method('/timer/*',self.oscHandler)

	def oscHandler(self,*args):
	# will receive message data unpacked in s,x,y
		for i in args:
			print(i)
			self.lastClicked=i+10
			master.update_idletasks()
			print(self.lastClicked)
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