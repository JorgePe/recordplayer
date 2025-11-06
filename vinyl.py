#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedDPM
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
from collections import deque

mTurntable = LargeMotor(OUTPUT_A)
mTurntable.stop()

#print('ramp_up_sp:   ', mTurntable.ramp_up_sp)
#print('ramp_down_sp: ', mTurntable.ramp_down_sp)

# default is zero

RampUp = 9000
RampDn = 9000
mTurntable.ramp_up_sp = RampUp    # ms to reach maxspeed (not target speed) 
mTurntable.ramp_down_sp = RampDn  # ms stop from maxspeed

# Arm:
#   Up = negative values
#   Down = positive values
mArm = LargeMotor(OUTPUT_B)
mArm.reset()

mPitch = MediumMotor(OUTPUT_C)
mPitch.reset()

sRecordEnd = ColorSensor(INPUT_2)

tsSpeed = TouchSensor(INPUT_1)

btn=Button()
sound = Sound()

# using SpeedDPM (degrees per minute)
# 1 RPM = 360 DPM
# SPEED = RPM * 360

SPEED_33 = int(33.333 * 360) + 1 + 10    # +1 to round up, +10 to adjust
SPEED_45 =45 * 360 + 20                  # +20 to adjust

# part of the pitch/speed perception also depends on...
# - the pressure applied by the needle
# - the length of the tonearm
# - how the record is "hold" (centered, horizontal, flat)


print(SPEED_33, SPEED_45)

def scratch():
    # temporarily adjust ramp up/down to better simulate a DJ hand
    # no luck yet
#    mTurntable.ramp_up_sp = 0.7
#    mTurntable.ramp_down_sp = 0.7
    mTurntable.ramp_up_sp = 0
    mTurntable.ramp_down_sp = 0

    if speed33:
        sp_percent = 14.8      # 12.3
        pause = 1.27           # 0.38
    else:
        sp_percent = int (14.8 * 45/33)
        pause = 1.27 * 45/33

    # baby scratch 2x
    # forth and back and forth

#    mTurntable.on(sp_percent, brake=False)
    mTurntable.on(SpeedDPM(SPEED), brake=False)
    sleep(pause)
#    mTurntable.on(-sp_percent * 1.05, brake=False)
    mTurntable.on(SpeedDPM(-SPEED*1.025), brake=False)
    sleep(pause*1.0)
#    mTurntable.on(sp_percent, brake=False)
    mTurntable.on(SpeedDPM(SPEED), brake=False)
    sleep(pause*1.25)
#   mTurntable.on(-sp_percent * 1.05, brake=False)
#    mTurntable.on(SpeedDPM(-SPEED*1.03), brake=False)
#    sleep(pause*0.88)
    
    # release
    
    if spinning:
        # ramp up/down here works much better
        mTurntable.ramp_up_sp = 850 # 0 900 550
        mTurntable.ramp_down_sp = 850 # 0 900 550
        mTurntable.on(SpeedDPM(SPEED), brake=False)
    
        # wait enough time for the motor to reach target speed then reset ramp up/down 
        sleep(1)  # perhaps too much
        mTurntable.ramp_up_sp = RampUp
        mTurntable.ramp_down_sp = RampDn
    else:
        mTurntable.stop()

def arm_down():
    print("DOWN")
#   move down to zero, carefully
    mArm.on_to_position(SpeedDPM(115), 0)    # 45..80+ slow and executes strange (in 2-steps) 

def arm_up():
    # needs attention, perhaps ramp up/down
    print("UP")
    mArm.on_to_position(4, -37)    # when too slow sometimes scratching happens

def start_spin():
    global spinning
    mTurntable.on(SpeedDPM(SPEED), brake=False)
    spinning = True

def stop_spin():
    global spinning
    mTurntable.stop()
    spinning = False

# move Arm support down

#arm_down()
mArm.on(5, brake=False)
mArm.wait_until_not_moving()
sleep(0.5)
mArm.position = 0       # mark as zero
arm_is_down = True

# read Speed Button

status_speed = tsSpeed.is_pressed
if status_speed:
    SPEED = SPEED_33
    speed33 = True
    print("33 RPM")
else:
    SPEED = SPEED_45
    speed33 = False
    print("45 RPM")

# start without picth offset
refPitch = 0

print("Start")
sound.beep()

spinning = False

# not sure if still needed, not used since 31/10/2025
count = 0
avg_sRecordEnd = 0
samples_sRecordEnd=deque([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


#play until it reaches the inner circle:
while True:

    if arm_is_down and spinning:
        value = sRecordEnd.reflected_light_intensity
        if count > 40:     # give enough time - 4s
            if count == 26:
                print("Monitoring color Sensor")
#            print(value, avg_sRecordEnd - value)

#            if (avg_sRecordEnd - value > 0.5) and (value > 30):         # 1.10 / 50
# or try dif > 3
            if (speed33 and value > 41) or ( (not speed33) and value > 48):
                # 41 not quite
                print("Finish")
                arm_up()
                arm_is_down = False
                stop_spin()

        count+=1
        samples_sRecordEnd.popleft()
        samples_sRecordEnd.append(value)
        avg_sRecordEnd = 0;
        for i in samples_sRecordEnd:
#            print(i, end=" ")
            avg_sRecordEnd += i
        avg_sRecordEnd = avg_sRecordEnd/10

#        print(sRecordEnd.reflected_light_intensity, avg_sRecordEnd)

    if not spinning:
        cur_status_speed = tsSpeed.is_pressed
        if cur_status_speed != status_speed:
            if speed33:
                SPEED = SPEED_33 + curPitch*6
                print("33 RPM")
            else:
                SPEED = SPEED_45 + curPitch*8    # 45/33 = 8.18
                print("45 RPM")
            print(SPEED)

            status_speed = cur_status_speed

    if btn.any():
        if btn.up:
            print("BTN UP")
            if arm_is_down:
                print("arm is down")
                # arm up
                arm_up()
                arm_is_down = False
        elif btn.down:
            print("BTN DOWN")
            if not arm_is_down:
                print("arm is not down")
                # clear history
                print("clear history")
                samples_sRecordEnd=deque([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                count=0
                avg_sRecordEnd=0
                arm_is_down = True
                # arm down
                arm_down()
        elif btn.left:
            print("BTN LEFT")
            if arm_is_down:
                print("scratch")
                scratch()
        elif btn.enter:
            print("BTN ENTER" )
            if spinning:
                stop_spin()
            else:
                start_spin()

        sleep(0.25)   # debounce time

    # read Pitch Dial
    curPitch = mPitch.position
    if curPitch != refPitch:
        # -180 .. +180
        # *2 = 360 = 3% of 33 RPM (1.5 RPM)
        # *5 = 7.5% (2.5 RPM) 
        print("curPitch:", curPitch)
        if speed33:
            SPEED = SPEED_33 + curPitch*6
        else:
            SPEED = SPEED_45 + curPitch*8    # 45/33 = 8.18
        print(SPEED)
        refPitch = curPitch

        if spinning:
            mTurntable.on(SpeedDPM(SPEED), brake=False)      # not sure if it changes speed while spinning

    sleep(0.1)


# we never get here but it's planned

# elevate again
arm_up()
sleep(2.5)
# stop spinning
stop_spin()

sleep(0.5)
print("End")
sound.beep()
mArm.stop()
