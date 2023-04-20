from adafruit_crickit import crickit
from adafruit_motor import stepper
import time

wave_count = 0
while wave_count < 5:
    crickit.servo_1.angle = 0
    time.sleep(0.5)
    crickit.servo_1.angle = 90
    time.sleep(0.5)
    wave_count = wave_count + 1




