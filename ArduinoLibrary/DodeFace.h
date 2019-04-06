//
// Created by MHerrera on 31/3/2019.
//

#ifndef ARDUINOLIBRARY_DODEFACE_H
#define ARDUINOLIBRARY_DODEFACE_H

#include <Servo.h>

class DodeFace {

public:
    void set(int pin, int t_cw1, int t_ccw1,int t_cw2, int t_ccw2, int t_cw3, int t_ccw3, int t_cw5, int t_ccw5, int t_cw_load, int t_ccw_load, int pwm_stp);
    DodeFace();
    DodeFace* down= nullptr;
    DodeFace* left= nullptr; // seen from outside
    DodeFace* right= nullptr;
    DodeFace* u_left= nullptr;
    DodeFace* u_right= nullptr;

    int t_cw1 =0;
    int t_ccw1=0;

    int t_cw2=0;
    int t_ccw2=0;

    int t_cw3=0;
    int t_ccw3=0;

    int t_cw5=0;
    int t_ccw5=0;

    int t_cw_load=0;
    int t_ccw_load=0;

    int pwm_stp=0;

    int pin=0;

    Servo servo;

};


#endif //ARDUINOLIBRARY_DODEFACE_H
