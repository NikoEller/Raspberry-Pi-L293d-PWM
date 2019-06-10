# This programm takes the measurments and then dicides where to drive

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

timer_motor_on = 1

# ________Motor_______-

Motor1A = 4
Motor1B = 7
Motor1E = 8

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

pwm = GPIO.PWM(Motor1E, 100)
pwm.start(0)

def goforward():
    # print("Going forwards")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)


    sleep(1)
    # print("Now stop")
    GPIO.output(Motor1E, GPIO.LOW)


if __name__ == '__main__':
    try:
        p = True
        goforward()
        while p:
            data = raw_input()
            if (data == 'w'):
                pwm.ChangeDutyCycle(25)
                GPIO.output(8, True)
                sleep(2)
                GPIO.output(8, False)
            if (data == "a"):
                pwm.ChangeDutyCycle(50)
                GPIO.output(8, True)
                sleep(2)
                GPIO.output(8, False)
            if (data == "d"):
                pwm.ChangeDutyCycle(75)
                GPIO.output(8, True)
                sleep(2)
                GPIO.output(8, False)
            if (data == "s"):
                pwm.ChangeDutyCycle(100)
                GPIO.output(8, True)
                sleep(2)
                GPIO.output(8, False)

            

    # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("")
        GPIO.cleanup()