/******************************************************************************
MAG3110.h
ADXL355 Library - MAG3110 Register Map
Original Creation Date: 10/10/2019
This file declares the ADXL355 class and registers
Development environment specifics:
	IDE: Visual Studio
	MAG3110 Breakout Version 1
Created by: Ljuboslav Boskic
******************************************************************************/

#ifndef ADXL355_h
#define ADXL355_h

#include "Arduino.h"
#include "Wire.h"

/******************************************************************************
//		ADXL355 I2C Address
******************************************************************************/

#define ADXL_I2C_Address 0x00

/******************************************************************************
		ADXL355 Registers

Addresses specified from Datasheet:
	Datasheet: ADXL354/ADXL355 (Rev. A)
	Analog Devices
******************************************************************************/
#define Devid_AD			0x00
#define Devid_MST			0x01
#define Partid				0x02
#define Revid				0x03
#define Status				0x04
#define FIFO_Entries		0x05
#define Temp2				0x06
#define Temp1				0x07
#define Xdata3				0x08
#define Xdata2				0x09
#define Xdata1				0x0A
#define Ydata3				0x0B
#define Ydata2				0x0C
#define Ydata1				0x0D
#define Zdata3				0x0E
#define Zdata2				0x0F
#define Zdata1				0x10
#define FIFO_data			0x11
#define Offset_X_H			0x1E
#define Offset_X_L			0x1F
#define Offset_Y_H			0x20
#define Offset_Y_L			0x21
#define Offset_Z_H			0x22
#define Offset_Z_L			0x23
#define Act_En				0x24
#define Act_Thresh_H		0x25
#define Act_Thresh_L		0x26
#define Act_Count			0x27
#define Filter				0x28
#define FIFO_Samples		0x29
#define Int_Map				0x2A
#define Sync				0x2B
#define Range				0x2C
#define Power_Ctl			0x2D
#define Self_Test			0x2E
#define Reset				0x2F

/******************************************************************************
		ADXL355 Range Definitions

Addresses specified from Datasheet:
	Datasheet: ADXL354/ADXL355 (Rev. A)
	Analog Devices
******************************************************************************/
Range_2g					01
Range_4g					10
Range_8g					11

/******************************************************************************
		ADXL355 Class
******************************************************************************/

class ADXL355
{
public:
	ADXL355();

	//Public Methods
	uint8_t readRegister(uint8_t address);
	void writeRegister(uint8_t address, uint8_t value);

	bool dataready();

	void readAdxl(float* x, float* y, float* z);

	void reset();
private:

};

