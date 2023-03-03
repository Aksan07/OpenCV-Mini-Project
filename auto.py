import pyautogui as pe
import os
import time
import subprocess
from demo import Gesture_Control
t=time.time
def open_file():
    pe.moveTo(405,583)
    pe.doubleClick()
def open_up_powerpoint():
    pe.keyDown('ctrl')
    pe.keyDown('alt')
    pe.keyDown('p')
    pe.keyUp('ctrl')
    pe.keyUp('alt')
    pe.keyUp('p')
    Gesture_Control()
    
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
    

open_up_powerpoint()

    










