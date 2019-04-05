//
// Created by MHerrera on 31/3/2019.
//

#include "DodeFast.h"

DodeFast::DodeFast(DodeFace currentFace) {
    this->currentFace = &currentFace;
}

DodeFast::DodeFast(){}

void DodeFast::printt() {
}


void DodeFast::down(){
    unsigned long currentMillis = 0;
    DodeFace *left = currentFace->left;
    DodeFace *right = currentFace->right;
    previousMillis = millis();
    Serial.println(left->pin);
    Serial.println(ccw);
    pwm.setPWM(left->pin,0,ccw);
    pwm.setPWM(right->pin,0,cw);

    ////cycle rotates dode
    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= FifthRotationFactor * (left->t_ccw)) {
            pwm.setPWM(left->pin,0,left->pwm_stp);
            Serial.println(left->pin);
            Serial.println(left->pwm_stp);
        }if (currentMillis - previousMillis >= FifthRotationFactor * (right->t_cw)) {
            pwm.setPWM(right->pin, 0, right->pwm_stp);
            Serial.println(right->pin);
            Serial.println(right->pwm_stp);

        }if (currentMillis - previousMillis >= FifthRotationFactor * (left->t_ccw) and
                   currentMillis - previousMillis >= FifthRotationFactor * (right->t_cw)) {

            break;
        }
    }

    previousMillis = currentMillis;

    pwm.setPWM(left->pin,0,cw);
    pwm.setPWM(right->pin,0,ccw);

    ////cycle resets zero position #1
    while(1){
        currentMillis = millis();
        if (currentMillis-previousMillis >= ThirdRotationFactor*(left->t_cw)){
            pwm.setPWM(left->pin,0,left->pwm_stp);
        }if(currentMillis-previousMillis >= ThirdRotationFactor*(right->t_ccw)) {
            pwm.setPWM(right->pin, 0, right->pwm_stp);
        }if (currentMillis-previousMillis >= ThirdRotationFactor*(left->t_cw) and
                  currentMillis-previousMillis >= ThirdRotationFactor*(right->t_ccw)) {
            break;
        }
    }

    previousMillis = currentMillis;


    DodeFace* u_left = currentFace->left->u_left;
    DodeFace* u_right = currentFace->right->u_right;

    pwm.setPWM(u_left->pin,0,cw);
    pwm.setPWM(u_right->pin,0,ccw);

    ////cycle resets zero position #2
    while(1){
        currentMillis = millis();
        if (currentMillis-previousMillis >= u_left->t_cw){
            pwm.setPWM(u_left->pin,0,u_left->pwm_stp);
        }else if(currentMillis-previousMillis >= u_right->t_ccw) {
            pwm.setPWM(u_left->pin, 0, u_right->pwm_stp);
        }else if (currentMillis-previousMillis >= u_left->t_cw and
                  currentMillis-previousMillis >= u_right->t_ccw) {
            break;
        }
    }

    previousMillis = currentMillis;


    DodeFace* u_left_og = currentFace->u_left;
    DodeFace* u_right_og = currentFace->u_right;
    DodeFace* up = u_left_og->u_right;
    pwm.setPWM(u_left_og->pin,0,ccw);
    pwm.setPWM(u_right_og->pin,0,cw);
    pwm.setPWM(up->pin,0,cw);


    ////cycle resets zero position #3
    while(1){
        currentMillis = millis();
        if (currentMillis-previousMillis >= u_left_og->t_ccw){
            pwm.setPWM(u_left_og->pin,0,u_left_og->pwm_stp);
        }else if(currentMillis-previousMillis >= u_right_og->t_cw) {
            pwm.setPWM(u_right_og->pin, 0, u_right_og->pwm_stp);
        }else if(currentMillis-previousMillis >= FifthRotationFactor*(up->t_cw)){
            pwm.setPWM(up->pin, 0, up->pwm_stp);
        }else if (currentMillis-previousMillis >= u_left_og->t_ccw and
                  currentMillis-previousMillis >= u_right_og->t_cw and
                  currentMillis-previousMillis >= FifthRotationFactor*(up->t_cw)) {
            break;
        }
    }

    previousMillis = currentMillis;


    DodeFace* up_right = currentFace->u_left->u_right->right;
    DodeFace* up_left = currentFace->u_left->u_right->left;
    DodeFace* up_u_right = currentFace->u_left->u_right->u_right;
    DodeFace* up_u_left = currentFace->u_left->u_right->u_left;
    pwm.setPWM(up_right->pin,0,cw);
    pwm.setPWM(up_left->pin,0,ccw);
    pwm.setPWM(up_u_right->pin,0,cw);
    pwm.setPWM(up_u_left->pin,0,ccw);


    ////cycle resets zero position #4
    while(1){
        currentMillis = millis();
        if (currentMillis-previousMillis >= SecondRotationFactor*up_right->t_cw){
            pwm.setPWM(up_right->pin,0,up_right->pwm_stp);
        }else if(currentMillis-previousMillis >= SecondRotationFactor*up_left->t_ccw) {
            pwm.setPWM(up_left->pin, 0, up_left->pwm_stp);
        }else if(currentMillis-previousMillis >= SecondRotationFactor*(up_u_left->t_ccw)){
            pwm.setPWM(up_u_left->pin, 0, up_u_left->pwm_stp);
        }else if(currentMillis-previousMillis >= SecondRotationFactor*(up_u_right->t_cw)) {
            pwm.setPWM(up_u_right->pin, 0, up_u_right->pwm_stp);
        }else if (currentMillis-previousMillis >= SecondRotationFactor*up_right->t_cw and
                  currentMillis-previousMillis >= SecondRotationFactor*up_left->t_ccw and
                  currentMillis-previousMillis >= SecondRotationFactor*(up_u_left->t_ccw) and
                  currentMillis-previousMillis >= SecondRotationFactor*(up_u_right->t_cw)) {
            break;
        }
    }

    previousMillis = currentMillis;


    DodeFace* down_u_left = currentFace->down->u_left;
    DodeFace* down_u_right = currentFace->down->u_right;
    DodeFace* up_down = currentFace->u_left->u_right->down;
    pwm.setPWM(down_u_left->pin,0,cw);
    pwm.setPWM(down_u_right->pin,0,ccw);
    pwm.setPWM(up_down->pin,0,cw);


    ////cycle resets zero position #5
    while(1){
        currentMillis = millis();
        if (currentMillis-previousMillis >= down_u_left->t_cw){
            pwm.setPWM(down_u_left->pin,0,down_u_left->pwm_stp);
        }else if(currentMillis-previousMillis >= SecondRotationFactor*down_u_right->t_ccw) {
            pwm.setPWM(down_u_right->pin, 0, down_u_right->pwm_stp);
        }else if(currentMillis-previousMillis >= FifthRotationFactor*(up_down->t_cw)){
            pwm.setPWM(up_down->pin, 0, up_down->pwm_stp);
        }else if (currentMillis-previousMillis >= down_u_left->t_cw and
                  currentMillis-previousMillis >= SecondRotationFactor*down_u_right->t_cw and
                  currentMillis-previousMillis >= FifthRotationFactor*(up_down->t_cw)) {
            break;
        }
    }

    previousMillis = currentMillis;


    pwm.setPWM(down_u_right->pin,0,cw);

    ////cycle resets zero position #6
    while(1){
        currentMillis = millis();
        if(currentMillis-previousMillis >= down_u_right->t_cw) {
            pwm.setPWM(down_u_right->pin, 0, down_u_right->pwm_stp);
            break;
        }
    }

    currentFace = currentFace->down;

}