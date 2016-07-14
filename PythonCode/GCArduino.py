# -*- coding: utf-8 -*-
"""
GCReader with a windows (tk) interface
Created on Sun Feb  7 09:50:02 2016

@author:
T. Andrew Mobley
Department of Chemistry
Noyce Science Center
Grinnell College
Grinnell, IA 50112
mobleyt@grinnell.edu
"""

import sys

try:
    import gcarduinoserial as gcaSerial
    import gcarduinowindow as gca
    import gcardglobals as gcaGlobals
except:
    print("Error Importing Configuration")
    sys.exit()

gcaGlobals.ard = gcaSerial.GCArduinoSerial()

gcaGlobals.mainwind = gca.gcArduinoWindow()

if not gcaGlobals.dataStation:
    gcaGlobals.mainwind.root.after(10, gca.connectToArduino)
    gcaGlobals.mainwind.root.after(50, gca.selectLiveTab)

gca.startMainLoop(gcaGlobals.mainwind)
