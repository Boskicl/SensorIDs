#adxl355_driver.py

from i2c_protocol import *
from time import sleep

ADXL355_I2C_ADDRESS = 0x1D
WHO_AM_I_Register = 0x01
WHO_AM_I_RESPONSE = 0x1D
Xdata3_Register = 0x08

Range_Register = 0x2C
Range_2g = 0x01
Range_4g = 0x02
Range_8g = 0x03

Power_CTL_Register = 0x2D
Measure = 0; # Measurement Mode
Standby = 1; # Standby Mode

dataOut = [0, 0, 0, 0] 

def ADXL355_check_status():
    i2c_write(ADXL355_I2C_ADDRESS, 1,WHO_AM_I_Register)
    returnedState = i2c_read(ADXL355_I2C_ADDRESS,1);
    if(returnedState==int("0x1d",0)):
        return True
    else:
        return False

def ADXL355_start(range_val,power_val):
    i2c_write_register(ADXL355_I2C_ADDRESS,Range_Register,range_val)
    sleep(0.1)
    i2c_write_register(ADXL355_I2C_ADDRESS,Power_CTL_Register,power_val)
    sleep(0.1)
    return 1

def ADXL355_read(range_val):
    i2c_write(ADXL355_I2C_ADDRESS, 1,Xdata3_Register)
    dataIn = i2c_read_register(ADXL355_I2C_ADDRESS,Xdata3_Register, 9)
    x = ((dataIn[0] << 12) | (dataIn[1] << 4) | (dataIn[2] >> 4))
    y = ((dataIn[3] << 12) | (dataIn[4] << 4) | (dataIn[5] >> 4))
    z = ((dataIn[6] << 12) | (dataIn[7] << 4) | (dataIn[8] >> 4))

    if x > 524287:
        x = (1048575-x)*-1
    if y > 524287:
        y = (1048575-x)*-1
    if z > 524287:
        z = (1048575-x)*-1

    dataOut[0] = True
    dataOut[1] = x / pow(2,int(range_val))
    dataOut[2] = y / pow(2,int(range_val))
    dataOut[3] = z / pow(2,int(range_val))

    return dataOut
