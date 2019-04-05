//
// Created by MHerrera on 31/3/2019.
//

#ifndef ARDUINOLIBRARY_DODEFACE_H
#define ARDUINOLIBRARY_DODEFACE_H


class DodeFace {

public:
    DodeFace(int pin, int t_cw, int t_ccw, int pwm_stp);
    DodeFace();
    DodeFace* down;
    DodeFace* left; // seen from outside
    DodeFace* right;
    DodeFace* u_left;
    DodeFace* u_right;

    int t_cw;
    int t_ccw;

    int pwm_stp;

    int pin;

};


#endif //ARDUINOLIBRARY_DODEFACE_H
