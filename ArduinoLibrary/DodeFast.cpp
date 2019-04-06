//
// Created by MHerrera on 31/3/2019.
//

#include "DodeFast.h"

DodeFast::DodeFast(DodeFace* currentFace) {
    this->currentFace = currentFace;
}

DodeFast::DodeFast(){}

void DodeFast::printt() {
}

void DodeFast::down(){
    move1(currentFace->left, currentFace->right);

}

void DodeFast::left(){
    move_aux(currentFace,ccw);

    unsigned long currentMillis = 0;
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_ccw2)) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }

    move1(currentFace->u_left, currentFace->down);
     delay(10);
    move_aux(currentFace,cw);
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_cw2)) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }
    delay(10);
}

void DodeFast::right(){

    move_aux(currentFace,cw);

    unsigned long currentMillis = 0;
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_cw2)) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }

    move1(currentFace->down, currentFace->u_right);
    delay(10);
    move_aux(currentFace,ccw);
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_ccw2)) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }
    delay(10);


}

void DodeFast::u_left(){

    move_aux(currentFace,ccw);

    unsigned long currentMillis = 0;
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_ccw2*1.7)) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }

    move1(currentFace->u_right, currentFace->left);
    delay(10);
    move_aux(currentFace,cw);
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_cw2)*1.7) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }
    delay(10);

}

void DodeFast::u_right(){
    move_aux(currentFace,cw);

    unsigned long currentMillis = 0;
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_cw2*1.7)) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }

    move1(currentFace->right, currentFace->u_left);
    delay(10);
    move_aux(currentFace,ccw);
    previousMillis = millis();

    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (currentFace->t_ccw2)*1.7) {
            move_aux(currentFace, currentFace->pwm_stp);
            break;
        }
    }
    delay(10);

}


void DodeFast::_AF(){}
void DodeFast::_F(){}
void DodeFast::_DFA(){}
void DodeFast::_IFA(){}
void DodeFast::_DFB(){}
void DodeFast::_IFB(){}
void DodeFast::_A(){}
void DodeFast::_DAA(){}
void DodeFast::_IAA(){}
void DodeFast::_DAB(){}
void DodeFast::_IAB(){}
void DodeFast::_AA(){}


void DodeFast::move_aux(DodeFace* face, int angle){
    if (face->pin<=11 and face->pin !=0 ){
        face->servo.write(angle);
    }
}
void DodeFast::move1(DodeFace *left, DodeFace *right) {

    unsigned long currentMillis = 0;
    previousMillis = millis();
    move_aux(left,ccw);
    move_aux(right,cw);

    ////cycle rotates dode
    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (left->t_ccw_load)) {
            move_aux(left,left->pwm_stp);

        }if (currentMillis - previousMillis >= (right->t_cw_load)) {
            move_aux(right,right->pwm_stp);

        }if (currentMillis - previousMillis >= (left->t_ccw_load) and
                   currentMillis - previousMillis >= (right->t_cw_load)) {
            break;
        }
    }
    delay(10);

    previousMillis = currentMillis;

    move_aux(left,cw);
    move_aux(right,ccw);

    ////cycle resets zero position #1
    while(1){
        currentMillis = millis();
        if (currentMillis-previousMillis >= (left->t_cw_load + 500)){
            move_aux(left,left->pwm_stp);
        }if(currentMillis-previousMillis >= (right->t_ccw_load + 500)) {
            move_aux(right, right->pwm_stp);
        }if (currentMillis-previousMillis >= (left->t_cw_load + 500) and
                  currentMillis-previousMillis >= (right->t_ccw_load + 500)) {
            break;
        }
    }

    delay(10);


    move_aux(left,ccw);
    move_aux(right,cw);

    previousMillis = currentMillis;

    ////cycle rotates dode
    while (true) {
        currentMillis = millis();
        if (currentMillis - previousMillis >= (left->t_ccw3)) {
            move_aux(left,left->pwm_stp);

        }if (currentMillis - previousMillis >= (right->t_cw3)) {
            move_aux(right,right->pwm_stp);

        }if (currentMillis - previousMillis >= (left->t_ccw3) and
             currentMillis - previousMillis >= (right->t_cw3)) {
            break;
        }
    }
    delay(10);
    return;

}