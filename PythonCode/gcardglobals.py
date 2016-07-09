# -*- coding: utf-8 -*-
"""
Module to hold various global variables for the GCReader project.

Created on Sun Feb 14 07:09:18 2016

@author:
T. Andrew Mobley
Department of Chemistry
Noyce Science Center
Grinnell College
Grinnell, IA 50112
mobleyt@grinnell.edu
"""
import serial_ports
import sys


def getPortDict():
    portList = serial_ports.serial_ports()
    portDict = dict(zip(range(len(portList)), portList))
    return portDict

if sys.platform.startswith('win'):
    platform = 'win'
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    platform = 'linux'
elif sys.platform.startswith('darwin'):
    platform = 'mac'
else:
    raise EnvironmentError('Unsupported platform')

# Main program objects
ard = None
mainwind = None
mainwindSize = "1500x1200"
mainwindPos = "50+50"
mainwindTit = "GC-Arduino Data Collection Interface"
dataStation = True

# Data notebook variables
liveframeHeight = 500
liveframeWidth = 900
dataframeHeight = 300
dataframeWidth = 550
colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
traceColor = 'black'
baselineColor = 'blue'

# File Information
outDirectory = '/Users/mobleyt/Desktop/GCard'
arduinoFile = "Not Connected"
helpfile = './Instructions.pdf'

# Arduino serial communications
arduinoCom = '/dev/cu.usbmodem1421'
portDict = getPortDict()
timeout = 0.1
baudrate = 57600
startString1 = ""
startString2 = ""

# Defaults for basic experimental variables
timeExper = "1"
comment = ""
channel = "1"
adcChoice = "ads1115"
adcChoices = {"arduino": "arduino", "ads1115": "ads1115"}

timeString = ""

# Processing variables
manPeakList = []
baseSelect = []
inBaseCt = 15
thresh = 0.001
gradThresh = 0.0005
areaChoice = "trapezoidal"
showBaseline = False

# Run flowcontrol booleans
multRuns = False
ch1Running = False
ch2Running = False
runRWgc = True

# Thread control
afterid = None
changeChannel = 999

# Instrument description
noChannels = 2
instrName = ['GC 1', 'GC 2']
