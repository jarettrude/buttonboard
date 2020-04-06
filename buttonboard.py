#!/usr/bin/env python3
#
# Licensed under the MIT license.  See full license in LICENSE file.
#
# Author: Jarett Rude

from gpiozero import LEDBoard, LED, Button
from time import sleep
from signal import pause
from subprocess import Popen, check_call
import glob

# DEFINE LEDS
allLEDS = LEDBoard(27, 22, 23, 24, 9, 25, 11, 8, 5, 12)
whiteLEDS = leds.value = (1,0,0,0,0,0,0,0,0,1)
greenLEDS = leds.value = (0,1,1,0,0,0,0,0,0,0)
blueLEDS = leds.value = (0,0,0,1,1,1,0,0,0,0)
purpleLEDS = leds.value = (0,0,0,0,0,0,1,1,1,0)
greenButtonLED = LED(7)

# DEFINE BUTTONS
redButton = Button(4)
blueButton = Button(14)
yellowButton = Button(15)
blackButton = Button(17)
greenButton = Button(18)
leftKnobButton = Button(26)
leftKnobButtonClk = Button(20)
leftKnobButtonCntClk = Button(19)
rightKnobButton = Button(16)
rightKnobButtonClk = Button(13)
rightKnobButtonCntClk = Button(6)

# SOUNDS
sdir = ('/home/pi/buttonboard/sounds/')
sounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
snum = len(glob.glob1(sdir,'*.mp3'))
smax = snum + 1
for s_count in sounds:
    print(s_count)
print(snum)
s_count = 0
def play():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        sounds[s_count]
    ]).wait()

# RED SOUNDS
redsdir = ('/home/pi/buttonboard/sounds/')
redsounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
redsnum = len(glob.glob1(sdir,'*.mp3'))
redsmax = snum + 1
for reds_count in redsounds:
    print(reds_count)
print(redsnum)
reds_count = 0
def redplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        redsounds[reds_count]
    ]).wait()

# BLUE SOUNDS
bluesdir = ('/home/pi/buttonboard/sounds/')
bluesounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
bluesnum = len(glob.glob1(sdir,'*.mp3'))
bluesmax = snum + 1
for blues_count in bluesounds:
    print(blues_count)
print(bluesnum)
blues_count = 0
def blueplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        bluesounds[blues_count]
    ]).wait()

# YELLOW SOUNDS
yellowsdir = ('/home/pi/buttonboard/sounds/')
yellowsounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
yellowsnum = len(glob.glob1(sdir,'*.mp3'))
yellowsmax = snum + 1
for yellows_count in yellowsounds:
    print(yellows_count)
print(yellowsnum)
yellows_count = 0
def yellowplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        yellowsounds[yellows_count]
    ]).wait()

# BLACK SOUNDS
blacksdir = ('/home/pi/buttonboard/sounds/')
blacksounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
blacksnum = len(glob.glob1(sdir,'*.mp3'))
blacksmax = snum + 1
for blacks_count in blacksounds:
    print(blacks_count)
print(blacksnum)
blacks_count = 0
def blackplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        blacksounds[blacks_count]
    ]).wait()

# GREEN SOUNDS
greensdir = ('/home/pi/buttonboard/sounds/')
greensounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
greensnum = len(glob.glob1(sdir,'*.mp3'))
greensmax = snum + 1
for greens_count in greensounds:
    print(greens_count)
print(greensnum)
greens_count = 0
def greenplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        greensounds[greens_count]
    ]).wait()

# LEFT SOUNDS
leftsdir = ('/home/pi/buttonboard/sounds/')
leftsounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
leftsnum = len(glob.glob1(sdir,'*.mp3'))
leftsmax = snum + 1
for lefts_count in leftsounds:
    print(lefts_count)
print(leftsnum)
lefts_count = 0
def leftplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        leftsounds[lefts_count]
    ]).wait()

# RIGHT SOUNDS
rightsdir = ('/home/pi/buttonboard/sounds/')
rightsounds = glob.glob("/home/pi/buttonboard/sounds/*.mp3")
rightsnum = len(glob.glob1(sdir,'*.mp3'))
rightsmax = snum + 1
for rights_count in rightsounds:
    print(rights_count)
print(rightsnum)
rights_count = 0
def rightplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        rightsounds[rights_count]
    ]).wait()


# LIGHTS CAMERA ACTION
while True:
    if redButton.is_pressed:
        allLEDS.on()
        redplay
        reds_count +=1
        if reds_count >= redsnum:
            reds_count = 0
    if blueButton.is_pressed:
        allLEDS.on()
        blueplay
        blues_count +=1
        if blues_count >= bluesnum:
            blues_count = 0
    if yellowButton.is_pressed:
        allLEDS.on()
        yellowplay
        yellows_count +=1
        if yellows_count >= yellowsnum:
            yellows_count = 0
    if blackButton.is_pressed:
        allLEDS.on()
        blackplay
        blacks_count +=1
        if blacks_count >= blacksnum:
            blacks_count = 0
    if greenButton.is_pressed:
        allLEDS.on()
        greenplay
        greens_count +=1
        if greens_count >= greensnum:
            greens_count = 0
    if leftKnobButton.is_pressed:
        allLEDS.on()
        leftplay
        lefts_count +=1
        if lefts_count >= leftsnum:
            lefts_count = 0
    if leftKnobButtonClk.is_pressed:
        allLEDS.on()
        leftplay
        lefts_count +=1
        if lefts_count >= leftsnum:
            lefts_count = 0
    if leftKnobButtonCntClk.is_pressed:
        allLEDS.on()
        leftplay
        lefts_count +=1
        if lefts_count >= leftsnum:
            lefts_count = 0
    if rightKnobButton.is_pressed:
            allLEDS.on()
            rightplay
            rights_count +=1
            if rights_count >= rightsnum:
                rights_count = 0
    if rightKnobButtonClk.is_pressed:
            allLEDS.on()
            rightplay
            rights_count +=1
            if rights_count >= rightsnum:
                rights_count = 0
    if rightKnobButtonCntClk.is_pressed:
            allLEDS.on()
            rightplay
            rights_count +=1
            if rights_count >= rightsnum:
                rights_count = 0


# SHUTDOWN BUTTON
def shutdown():
    check_call(['sudo', 'poweroff'])
shutdown_btn = Button(21, hold_time=2)
shutdown_btn.when_held = shutdown

pause()
