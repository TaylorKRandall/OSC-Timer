#!/usr/bin/python

import tkinter as tk
import tkinter.font
# import tkinter.ttk

def quit(*args):
	root.destroy()

root=tk.Tk()
root.attributes('-fullscreen',True,'-titlepath','timer.py')
root['bg']='black'
root.bind('x',quit)
# print(dir(root))
lbl=tk.Label(text='test',fg='white',bg='black')
lbl.place(relx=0.5, rely=0.5, anchor='center')
root.mainloop()

print('all is good!')