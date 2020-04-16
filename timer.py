#!/usr/bin/python

import tkinter as tk
import tkinter.font
from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

finished=False
IP='192.168.0.7'
PORT=53000
counter=0

def oscHandler(*args):
	# will receive message data unpacked in s,x,y
	global counter
	for i in args:
		print(i)
		counter+=i
		print(counter)
		print('exiting handler...')


def quit(*args):
	root.destroy()
	finished=True

root=tk.Tk()
root.attributes('-fullscreen',True,'-titlepath','timer.py')
root['bg']='black'
root.bind('x',quit)
lbl=tk.Label(text=counter,fg='white',bg='black')
lbl.place(relx=0.5, rely=0.5, anchor='center')

print('defined root...')
print(dir(root.mainloop))

osc_startup()
osc_udp_server(IP,PORT,'OSCtimer')
osc_method('/timer/*',oscHandler)

while not finished:
	#...
	osc_process()
	root.update_idletasks()
	root.update()
	#...
osc_terminate()