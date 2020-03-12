#!/usr/bin/env python3
#
# Licensed under the MIT license.  See full license in LICENSE file.
#
# Author: Jarett Rude

from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause
from subprocess import Popen, check_call
import glob

leds = LEDBoard(27, 22, 23, 24, 9, 25, 11, 8, 5, 12)
button = Button(21)

sdir = ('/home/pi/buttonboard/sounds/')
sounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
snum = len(glob.glob1(sdir,'*.mp3'))
smax = snum + 1
# sounds = ['/home/pi/buttonboard/sounds/coin.mp3', '/home/pi/buttonboard/sounds/1_Up.mp3']

for s in sounds:
    print(s)

s_count = 0

def play():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        sounds[s_count]
    ]).wait()

while True:

    button.when_pressed = leds.on
    button.when_released = play
    s_count +=1
    if s_count == smax:
        s_count = 0


# SHUTDOWN BUTTON

#def shutdown():
#    check_call(['sudo', 'poweroff'])

#shutdown_btn = Button(21, hold_time=2)
#shutdown_btn.when_held = shutdown

pause()
