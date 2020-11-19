import time, serial, sys, getopt

start_register = 75
mode_register = 76
setpoint0_register = 63
setpoint1_register = 64
setpoint2_register = 65
setpoint3_register = 66
setpointtime_register = 71

# profile definition
# [[temp1, time1], [temp2, time2], ... , [tempn, timen]]
profile = [[50, 10], [150, 10]]

# pairs are [temp, time] but you can redefine that order here and rewrite the profile above
tempindex = 0
timeindex = 1

# setup modbus controller
import minimalmodbus
controller = minimalmodbus.Instrument('COM21', 1)
controller.serial.baudrate = 115200
controller.serial.timeout

# START HEATING
controller.write_register(start_register, 1)
# set the controller to setpoint internally because we are using an externally defined profile
controller.write_register(mode_register, 0)

# run each step of the profile
for step in profile:
    # report to command line
    print("Heating to " + str(step[tempindex]), " for " + str(step[timeindex]) + " seconds")
    # set the setpoints (scaled by 10 because the modbus registers need ints but we need decimal pt percision)
    controller.write_register(setpoint0_register, step[tempindex] * 10)
    controller.write_register(setpoint1_register, step[tempindex] * 10)
    controller.write_register(setpoint2_register, step[tempindex] * 10)
    controller.write_register(setpoint3_register, step[tempindex] * 10)
    # stay at setpoint for step time
    time.sleep(step[timeindex])

# stop after profile
controller.write_register(start_register, 0)
# cooling will trigger automatically until the temp is below the cooldown threshold