#******************************************************************************
# MAG3110 
# Original Creation Date: 3/10/2020
# SparkFun Triple Axis Magnetometer Breakout - MAG3110
# Development environment specifics:
#   	IDE: Visual Studio
#	    Python Version: 3.6.8
# Created by: Ljuboslav Boskic
#*****************************************************

from i2c_protocol import *

MAG3110_I2C_ADDRESS = 0x0E
MAG3110_DR_STATUS = 0x00
MAG3110_OUT_X_MSB = 0x01
MAG3110_WHO_AM_I = 0x07
MAG3110_CTRL_REG1 = 0x10

x = y = z = 0
dataOut = [0, 0, 0, 0] 

def MAG3110_init(): #Initiate the Sensor 
    i2c_write(MAG3110_I2C_ADDRESS, 1,MAG3110_WHO_AM_I)
    returnedState = i2c_read(MAG3110_I2C_ADDRESS,1);
    if(returnedState==int("0xc4",0)):
        return True
    else:
        return False

def MAG3110_check_status(): # Check Status 
    i2c_write(MAG3110_I2C_ADDRESS, 1,MAG3110_WHO_AM_I)
    returnedState = i2c_read(MAG3110_I2C_ADDRESS,1);
    if(returnedState==int("0xc4",0)):
        return True
    else:
        return False

def MAG3110_enable_run_mode(): # Turn on Run/Measure Mode
    status = MAG3110_check_status()
    if (status) :
        i2c_write(MAG3110_I2C_ADDRESS, 1,MAG3110_CTRL_REG1)
        currentReg = i2c_read(MAG3110_I2C_ADDRESS,1)
        newReg = (currentReg | 1)
        i2c_write_register(MAG3110_I2C_ADDRESS, MAG3110_CTRL_REG1, newReg)
        return True
    else:
        return False

def MAG3110_read_sensor(): # Read MAG3110 in mT
    status = MAG3110_check_status()
    if (status):
        i2c_write(MAG3110_I2C_ADDRESS, 1,MAG3110_DR_STATUS)
        if((i2c_read(MAG3110_I2C_ADDRESS,1)&1000)>>3):
            dataIn = i2c_read_register(MAG3110_I2C_ADDRESS,MAG3110_OUT_X_MSB, 6)
            x = ((dataIn[0] << 8) | (dataIn[1]))
            y = ((dataIn[2] << 8) | (dataIn[3]))
            z = ((dataIn[4] << 8) | (dataIn[5]))
            if x > 32767:
                x = (65535-x)*-1
            if y > 32767:
                y = (65535-y)*-1
            if z > 32767:
                z = (65535-z)*-1
            dataOut[0] = True
            dataOut[1] = x
            dataOut[2] = y
            dataOut[3] = z

            return dataOut
        else:
            dataOut[0] = False
            dataOut[1] = 0
            dataOut[2] = 0
            dataOut[3] = 0

            return dataOut
    else:
        dataOut[0] = False
        dataOut[1] = 0
        dataOut[2] = 0
        dataOut[3] = 0

        return dataOut
