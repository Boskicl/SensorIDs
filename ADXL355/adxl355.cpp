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

#include <Arduino.h>
#include "adxl355.h"
#include <Wire.h>
#include <math.h>

ADXL355::ADXL355() {
    // Initial Values
}

// bool ADXL355::initalizeADXL() {
//     if (readRegister(WHO_AM_I) != WHO_AM_I_RESPC) { //Could not find ADXL355
//     // Serial.println("Could not find ADXL355")
//         return false;
//     }
//     else // Successfully initialized
//     {
//         reset();
//         return true;
//     }
// }

// uint8_t ADXL355::readRegister(uint8_t address){
//   uint8_t output;

//   Wire.beginTransmission(ADXL355_I2C_ADDRESS);
//   Wire.write(address);
//   Wire.endTransmission();

//   delayMicroseconds(2);

//   Wire.requestFrom(ADXL355_I2C_ADDRESS, 1);
//   while(Wire.available())
//   {
// 	output = Wire.read();
//   }

//   return output;
// }

// For all Communication for ADXL355 use this - can set range and other settings
void ADXL355::writeRegist(uint8_t address, uint8_t value) {
    Wire.beginTransmission(ADXL355_I2C_ADDRESS);                    // Write to the device address of th ADXL355
    Wire.write(address);
    Wire.write(value);
    Wire.endTransmission();
}

// Start Communications and set the proper address/values 
void ADXL355::StartADXL(uint8_t address, uint8_t value, uint8_t address2, uint8_t value2) {
    writeRegist(address,address);
    delay(100);
    writeRegist(address2,value2);
    delay(100);
    
}

// Scalefactor- adjusts depending on using 2G, 4G, or 8G setting
float ADXL355::Scalefactor(int g) {
    /******************************************************************************
    (input)  int g   =   Range setting of 2g,4g,8g, input either 2,4,8
    (return) scale   =   float of scale factor used to calculate Gs 
    ******************************************************************************/
    float scale;
    if (g==2)
        scale = 4 / (pow(2,20)-1); //2g
    if (g==4)
        scale = 8 / (pow(2,20)-1); //4g
    if (g==8)
        scale = 16 / (pow(2,20)-1); //8g
    return (scale);


}

// readACCELL- For getting the value in the x/y/z direction of the Gs applied
void ADXL355::readACCEL(float* x, float* y, float* z, int G) {
    /******************************************************************************
    (input) *x   =   This value is returned, input is just a float and a variable for the x value
    (input) *y   =   This value is returned, input is just a float and a variable for the y value
    (input) *z   =   This value is returned, input is just a float and a variable for the z value
    (input) G    =   int G is the value you give either 2,4,8 for the Scalefactor function to adjust to right 2g,4g,8g setting
    (output) *x   =   Returns X value in Gs, based on certain setting set by G input/Scalefactor
    (output) *y   =   Returns Y value in Gs, based on certain setting set by G input/Scalefactor
    (output) *z   =   Returns Z value in Gs, based on certain setting set by G input/Scalefactor
    ******************************************************************************/

    // Start readout at address
    double values[3];
    Wire.beginTransmission(ADXL355_I2C_ADDRESS);
    Wire.write(Xdata3);                             // Read first byte, auto increments to read rest
    Wire.endTransmission();
    Wire.requestFrom(ADXL355_I2C_ADDRESS,9,true);   // Read 9 bytes, 3 from each axis
    byte x1, x2, x3;
    for (int i = 0; i <3; ++i){
        x3 = Wire.read();
        x2 = Wire.read();
        x1 = Wire.read();
        unsigned long tempV = 0;
        unsigned long value = 0;
        value = x3;
        value <<= 12;
        tempV = x2;
        tempV <<= 4;
        value |= tempV;
        if (x3 & 0x80){
            value |= 0xFFF00000;
        }
        tempV =x1;
        tempV >>=4;
        value |= tempV;
        // Scalefactor(G);
        values[i] =  Scalefactor(G) * (long)value;
        // Read each axis and return value
        *x = (float) values[0];
        *y = (float) values[1];
        *z = (float) values[2];
    }
    
}

// Reset ADXL355
void ADXL355::reset() {
    writeRegist(RESET,RESET_ALL);
}