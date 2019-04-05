//
// Created by MHerrera on 31/3/2019.
//

#include "DodeFace.h"

DodeFace::DodeFace(int pin, int t_cw, int t_ccw, int pwm_stp){
    this->pin = pin;
    this->t_cw = t_cw;
    this->t_ccw = t_ccw;
    this->pwm_stp = pwm_stp;
}

DodeFace::DodeFace() {}
