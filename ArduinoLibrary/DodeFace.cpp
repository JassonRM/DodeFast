//
// Created by MHerrera on 31/3/2019.
//

#include "DodeFace.h"


void DodeFace::set(int pin, int t_cw1, int t_ccw1,int t_cw2, int t_ccw2, int t_cw3, int t_ccw3, int t_cw5, int t_ccw5, int t_cw_load, int t_ccw_load, int pwm_stp){
    this->pin = pin;
    this->t_cw1 = t_cw1;
    this->t_ccw1 = t_ccw1;
    this->t_cw2 = t_cw2;
    this->t_ccw2 = t_ccw2;
    this->t_cw3 = t_cw3;
    this->t_ccw3 = t_ccw3;
    this->t_cw5 = t_cw5;
    this->t_ccw5 = t_ccw5;
    this->t_cw_load = t_cw_load;
    this->t_ccw_load = t_ccw_load;
    this->pwm_stp = pwm_stp;
    this->servo.attach(pin);
}

DodeFace::DodeFace() {}
