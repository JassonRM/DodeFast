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
    DodeFast(DodeFace* currentFace);
    DodeFast();

    DodeFace* currentFace;
    Adafruit_PWMServoDriver pwm;
    unsigned long previousMillis;
    int cw = 0;
    int ccw = 300;


    void _AF();
    void _F();
    void _DFA();
    void _IFA();
    void _DFB();
    void _IFB();
    void _A();
    void _DAA();
    void _IAA();
    void _DAB();
    void _IAB();
    void _AA();

    void down();
    void left();
    void right();
    void u_left();
    void u_right();


    void move_aux(DodeFace*, int);
    void move1(DodeFace *left, DodeFace *right);
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
