#******************************************************************************
# TCA9548A I2C Multiplexer
# Original Creation Date: 3/10/2020
# Way to get up to 8 same-address I2C devices to one microcontroller
# Development environment specifics:
#   	IDE: Visual Studio
#	    Python Version: 3.6.8
# Created by: Ljuboslav Boskic
#*****************************************************

from i2c_protocol import *

TCA9548A_ADDRESS = 0x70 # Address of TCA9548A
TCA9548A_Pin_0 = 1
TCA9548A_Pin_1 = 2
TCA9548A_Pin_2 = 4
TCA9548A_Pin_3 = 8
TCA9548A_Pin_4 = 16
TCA9548A_Pin_5 = 32
TCA9548A_Pin_6 = 64
TCA9548A_Pin_7 = 128

def TCA9548A_set_Pin_ch_0():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_0)

def TCA9548A_set_Pin_ch_1():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_1)

def TCA9548A_set_Pin_ch_2():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_2)

def TCA9548A_set_Pin_ch_3():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_3)

def TCA9548A_set_Pin_ch_4():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_4)

def TCA9548A_set_Pin_ch_5():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_5)

def TCA9548A_set_Pin_ch_6():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_6)

def TCA9548A_set_Pin_ch_7():
    i2c_write(TCA9548A_ADDRESS, 1,TCA9548A_Pin_7)
