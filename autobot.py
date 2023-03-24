import pyautogui as pe
import os
import time
import subprocess
from demo import Gesture_Control
t=time.time
def open_file():
    pe.moveTo(405,583)
    pe.doubleClick()
    
def start_presentation():
    pe.keyDown('f5')
    pe.keyUp('f5')
    
def move_left():
    pe.press('left')
    time.sleep(1)
def move_right():
    pe.press('right')
    time.sleep(1)
def close_presentation():
    pe.press('esc') 

pe.press("win")
    # pe.press('s')
    # pe.keyUp('win')
    # pe.keyUp('s')

pe.write(' Hand Gesture Mini Project',interval=0.2)
pe.press("enter")
Gesture_Control()
    










