//
// Created by MHerrera on 31/3/2019.
//

#ifndef ARDUINOLIBRARY_DODEFAST_H
#define ARDUINOLIBRARY_DODEFAST_H

#include "DodeFace.h"
#include <Adafruit_PWMServoDriver.h>
#include "Arduino.h"
class DodeFast {

public:
    DodeFast(DodeFace currentFace);
    DodeFast();

    DodeFace* currentFace;
    Adafruit_PWMServoDriver pwm;
    unsigned long previousMillis;
    int cw = 400;
    int ccw = 300;
    int FifthRotationFactor = 5;
    int ThirdRotationFactor = 3;
    int SecondRotationFactor = 2;
    /*
    void AF();
    void F();
    void DFA();
    void IFA();
    void DFB();
    void IFB();
    void A();
    void DAA();
    void IAA();
    void DAB();
    void IAB();
    void AA();
    */
    void down();
    void printt();
private:
    /*
    void left();
    void right();
    void u_left();
    void u_right();
    */
};


#endif //ARDUINOLIBRARY_DODEFAST_H
