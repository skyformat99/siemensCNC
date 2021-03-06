#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
from tkinter import *

#Siemens communication
# India, Bangalore
# 2017/02/15

__author__ = "Daniel Merelas"
__license__ = "GNU3"
__version__ = "1.0"
__email__ = "daniel@merelas.es"

def comm ():
    return

class machine:
    machineID = "M1";
    machineIP = "192.168.101.11";
    machinePort = "3011";
    machineTimeout = "5";
    hostID = "H1";
    hostPort = "3010";

class machineStatus:
    host="";
    machine="";
    orderNum="";
    machineMode="";
    machineStatus="";
    ncProgram="";
    clampCubeSide="";
    dockPos="";
    dockPosStatus="";
    wpc="";
    wpcStatus="";
    resInt1="";
    resInt2="";
    resByte="";

#Instancia
window = Tk()
window.title('Nixo - V' + __version__)
window.resizable(False, False)

#Centering the window in the screen
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x, y))

#Config button
configButton = Button(window, text='Config communication', command=comm, width=40)
configButton.grid(row=1, column=3)

#Main window
window.mainloop()

