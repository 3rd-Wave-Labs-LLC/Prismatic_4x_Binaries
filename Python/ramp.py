import time, serial, sys
import minimalmodbus

START_REG = 75
MODE_REG = 76
TEMP0_REG = 77
TEMP1_REG = 78
TEMP2_REG = 79
TEMP3_REG = 80
SETPOINT0_REG = 63
SETPOINT1_REG = 64
SETPOINT2_REG = 65
SETPOINT3_REG = 66

############### SCRIPT CONFIGURATION ###############
# SET COM PORT HERE
COM_PORT = 'COM7'

# SET SLOPE HERE (Degrees C / second)
SLOPE = 1

# SET GOAL SETPOINT HERE (Degrees C)
GOAL = 80

# SET WRITE DELAY HERE
# decrease this if you want a smoother slope at
WRITE_DELAY = .05
#####################################################

# setup modbus controller
try:
    controller = minimalmodbus.Instrument(COM_PORT, 1)
except:
    print(f'failed to connect on port {COM_PORT}')
    print(f'edit the script to use the correct com port')
    exit()
controller.serial.baudrate = 115200
controller.serial.timeout



# retrieve the starting temps (Degrees C)
start_temp0 = controller.read_register(TEMP0_REG) / 10
start_temp1 = controller.read_register(TEMP1_REG) / 10
start_temp2 = controller.read_register(TEMP2_REG) / 10
start_temp3 = controller.read_register(TEMP3_REG) / 10

setpoint0 = start_temp0
setpoint1 = start_temp1
setpoint2 = start_temp2
setpoint3 = start_temp3

# calculate the total time for each ramp (nanoseconds)

SLOPE_NS = SLOPE / 1000000000

temp_change0 = (GOAL - start_temp0)
temp_change1 = (GOAL - start_temp1)
temp_change2 = (GOAL - start_temp2)
temp_change3 = (GOAL - start_temp3)

ramp_ns0 = (temp_change0 / SLOPE_NS)
ramp_ns1 = (temp_change1 / SLOPE_NS)
ramp_ns2 = (temp_change2 / SLOPE_NS)
ramp_ns3 = (temp_change3 / SLOPE_NS)

start_time = time.time_ns()
controller.write_register(MODE_REG, 0) # SETPOINT MODE
controller.write_register(START_REG, 1) # START HEATERS
while True:
    try:
        now = time.time_ns()
        elapsed = now - start_time

        if setpoint0 <= GOAL:
            setpoint0 = (elapsed * (temp_change0 / ramp_ns0) + start_temp0)
            controller.write_register(SETPOINT0_REG, setpoint0 * 10)
            print(setpoint0)
        if setpoint1 <= GOAL:
            setpoint1 = (elapsed * (temp_change1 / ramp_ns1) + start_temp1)
            controller.write_register(SETPOINT1_REG, setpoint1 * 10)
            print(setpoint1)
        if setpoint2 <= GOAL:
            setpoint2 = (elapsed * (temp_change2 / ramp_ns2) + start_temp2)
            controller.write_register(SETPOINT2_REG, setpoint2 * 10)
            print(setpoint2)
        if setpoint3 <= GOAL:
            setpoint3 = (elapsed * (temp_change3 / ramp_ns3) + start_temp3)
            controller.write_register(SETPOINT3_REG, setpoint3 * 10)
            print(setpoint3)

        print('================\n')

        if (setpoint0 >= GOAL) and (setpoint1 >= GOAL) and (setpoint2 >= GOAL) and (setpoint3 >= GOAL):
            break

        time.sleep(WRITE_DELAY)
    except KeyboardInterrupt:
        print('ramp canceled')
        exit(0)
    except Exception as e:
        print(e)




