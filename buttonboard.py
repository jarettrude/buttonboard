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

# SHUTDOWN BUTTON
def shutdown():
    check_call(['sudo', 'poweroff'])
shutdown_btn = Button(21, hold_time=2)
shutdown_btn.when_held = shutdown

# DEFINE LEDS
allLEDS = LEDBoard(27, 22, 23, 24, 9, 25, 11, 8, 5, 12)
def whiteLEDS():
    allLEDS.value = (1,0,0,0,0,0,0,0,0,1)
def greenLEDS():
    allLEDS.value = (0,1,1,0,0,0,0,0,0,0)
def blueLEDS():
    allLEDS.value = (0,0,0,1,1,1,0,0,0,0)
def purpleLEDS():
    allLEDS.value = (0,0,0,0,0,0,1,1,1,0)
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

# RED SOUNDS
reddir = ('/home/pi/buttonboard/sounds/red/')
redsound = glob.glob("/home/pi/buttonboard/sounds/red/*.mp3")
rednum = len(glob.glob1(reddir,'*.mp3'))
redmax = rednum + 1
for red_count in redsound:
    print(red_count)
print(rednum)
red_count = 0
def redplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        redsound[red_count]
    ]).wait()
    
# BLUE SOUNDS
bluedir = ('/home/pi/buttonboard/sounds/blue/')
bluesound = glob.glob("/home/pi/buttonboard/sounds/blue/*.mp3")
bluenum = len(glob.glob1(bluedir,'*.mp3'))
bluemax = bluenum + 1
for blue_count in bluesound:
    print(blue_count)
print(bluenum)
blue_count = 0
def blueplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        bluesound[blue_count]
    ]).wait()

# YELLOW SOUNDS
yellowdir = ('/home/pi/buttonboard/sounds/yellow/')
yellowsound = glob.glob("/home/pi/buttonboard/sounds/yellow/*.mp3")
yellownum = len(glob.glob1(yellowdir,'*.mp3'))
yellowmax = yellownum + 1
for yellow_count in yellowsound:
    print(yellow_count)
print(yellownum)
yellow_count = 0
def yellowplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        yellowsound[yellow_count]
    ]).wait()

# BLACK SOUNDS
blackdir = ('/home/pi/buttonboard/sounds/black/')
blacksound = glob.glob("/home/pi/buttonboard/sounds/black/*.mp3")
blacknum = len(glob.glob1(blackdir,'*.mp3'))
blackmax = blacknum + 1
for black_count in blacksound:
    print(black_count)
print(blacknum)
black_count = 0
def blackplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        blacksound[black_count]
    ]).wait()

# GREEN SOUNDS
greendir = ('/home/pi/buttonboard/sounds/green/')
greensound = glob.glob("/home/pi/buttonboard/sounds/green/*.mp3")
greennum = len(glob.glob1(greendir,'*.mp3'))
greenmax = greennum + 1
for green_count in greensound:
    print(green_count)
print(greennum)
green_count = 0
def greenplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        greensound[green_count]
    ]).wait()

# LEFT KNOB SOUNDS
leftknobdir = ('/home/pi/buttonboard/sounds/leftknob/')
leftknobsound = glob.glob("/home/pi/buttonboard/sounds/leftknob/*.mp3")
leftknobnum = len(glob.glob1(leftknobdir,'*.mp3'))
leftknobmax = leftknobnum + 1
for leftknob_count in leftknobsound:
    print(leftknob_count)
print(leftknobnum)
leftknob_count = 0
def leftknobplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        leftknobsound[leftknob_count]
    ]).wait()

# RIGHT KNOB SOUNDS
rightknobdir = ('/home/pi/buttonboard/sounds/rightknob/')
rightknobsound = glob.glob("/home/pi/buttonboard/sounds/rightknob/*.mp3")
rightknobnum = len(glob.glob1(rightknobdir,'*.mp3'))
rightknobmax = rightknobnum + 1
for rightknob_count in rightknobsound:
    print(rightknob_count)
print(rightknobnum)
rightknob_count = 0
def rightknobplay():
    Popen([
        'bash', '/home/pi/buttonboard/lightshowpiMods/play',
        rightknobsound[rightknob_count]
    ]).wait()

# LIGHTS CAMERA ACTION
while True:
    allLEDS.off()
    if redButton.is_pressed:
        allLEDS.on()
        redplay()
        red_count +=1
        print(red_count)
        if red_count >= rednum:
            red_count = 0
    if blueButton.is_pressed:
        allLEDS.on()
        blueplay()
        blue_count +=1
        print(blue_count)
        if blue_count >= bluenum:
            blue_count = 0
    if yellowButton.is_pressed:
        allLEDS.on()
        yellowplay()
        yellow_count +=1
        print(yellow_count)
        if yellow_count >= yellownum:
            yellow_count = 0
    if blackButton.is_pressed:
        allLEDS.on()
        blackplay()
        black_count +=1
        print(black_count)
        if black_count >= blacknum:
            black_count = 0
    if greenButton.is_pressed:
        allLEDS.on()
        greenButtonLED.on()
        greenplay()
        greenButtonLED.off()
        green_count +=1
        print(green_count)
        if green_count >= greennum:
            green_count = 0
    if leftKnobButton.is_pressed:
        allLEDS.on()
        leftknobplay()
        leftknob_count +=1
        print(leftknob_count)
        if leftknob_count >= leftknobnum:
            leftknob_count = 0
    if leftKnobButtonClk.is_pressed:
        allLEDS.on()
        leftknobplay()
        leftknob_count +=1
        print(leftknob_count)
        if leftknob_count >= leftknobnum:
            leftknob_count = 0
    if leftKnobButtonCntClk.is_pressed:
        allLEDS.on()
        leftknobplay()
        leftknob_count +=1
        print(leftknob_count)
        if leftknob_count >= leftknobnum:
            leftknob_count = 0
    if rightKnobButton.is_pressed:
        allLEDS.on()
        rightknobplay()
        rightknob_count +=1
        print(rightknob_count)
        if rightknob_count >= rightknobnum:
            rightknob_count = 0
    if rightKnobButtonClk.is_pressed:
        allLEDS.on()
        rightknobplay()
        rightknob_count +=1
        print(rightknob_count)
        if rightknob_count >= rightknobnum:
            rightknob_count = 0
    if rightKnobButtonCntClk.is_pressed:
        allLEDS.on()
        rightknobplay()
        rightknob_count +=1
        print(rightknob_count)
        if rightknob_count >= rightknobnum:
            rightknob_count = 0

pause()