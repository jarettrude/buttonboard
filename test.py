from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause
from subprocess import Popen, check_call

leds = LEDBoard(27, 22, 23, 24, 9, 25, 11, 8, 5, 12)
button = Button(21)

def play():
    Popen([
        'bash', '/home/pi/buttonboard/play',
        '/home/pi/buttonboard/sounds/coin.mp3'
    ]).wait()


button.when_pressed = leds.on
button.when_released = play


# SHUTDOWN BUTTON

#def shutdown():
#    check_call(['sudo', 'poweroff'])

#shutdown_btn = Button(21, hold_time=2)
#shutdown_btn.when_held = shutdown

pause()