from threading import Thread
import time
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from keyboard import Keyboard
import os
import pathlib

## Keyboard
kb = Thread(target=Keyboard)
kb.start()

## Unity        
#thispath = pathlib.Path().resolve()
#os.startfile( f'"{thispath}\pick&place1.2\Human - Robot Collaboration.exe"')