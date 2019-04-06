
#define LED1 2
#define LED2 4
#define LED3 7
#define LED4 8
#define LED5 12
#define LED6 13



#include "C:\Users\mherr\Proyectos\DodeFast\ArduinoLibrary\DodeFast.cpp"
#include "C:\Users\mherr\Proyectos\DodeFast\ArduinoLibrary\DodeFast.h"
#include "C:\Users\mherr\Proyectos\DodeFast\ArduinoLibrary\DodeFace.cpp"
#include "C:\Users\mherr\Proyectos\DodeFast\ArduinoLibrary\DodeFace.h"


  //Instanciate all faces
  DodeFace* bottom = new DodeFace();
  DodeFace* bottom_down = new DodeFace();
  DodeFace* bottom_left = new DodeFace();
  DodeFace* bottom_right = new DodeFace();
  DodeFace* bottom_u_left = new DodeFace();
  DodeFace* bottom_u_right = new DodeFace();

  DodeFace* top = new DodeFace();
  DodeFace* top_down = new DodeFace();
  DodeFace* top_left = new DodeFace();
  DodeFace* top_right = new DodeFace();
  DodeFace* top_u_left = new DodeFace();
  DodeFace* top_u_right = new DodeFace();

  DodeFast dode;


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
  pinMode(LED1,OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3,OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5,OUTPUT);
  pinMode(LED6, OUTPUT);
  initialize();
  led6();
}

void loop() {
  // put your main code here, to run repeatedly:
  String data;
  if(Serial.available()>0){
      data = Serial.readString();
      Serial.println("Recibido: '" + data + "'");
      }
      if(data == "AF"){
        led1();
        }
      if(data == "F"){
        led1();
        }
      if(data == "DFA"){
        led5();
        }
      if(data == "IFA"){
        led4();
        }
      if(data == "DFB"){
        led5();
        }
      if(data == "IFB"){
        led4();
        }
      if(data == "A"){
        led1();
        }
      if(data == "DAA"){
        led2();
        }
      if(data == "IAA"){
        led3();
        }
      if(data == "AL"){
        led6();
        }
      if(data == "L"){
        led7();
        }
      if(data == "K"){
        led8();
        }
        if(data == "P"){
        led9();
        }

        
        
          
}

void allOff(){
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, LOW);
  digitalWrite(LED5, LOW);
  }

void led1(){
  dode.down();
  allOff();
  digitalWrite(LED6, HIGH);
  delay(500);
  }

void led2(){
  dode.left();
  allOff();
  digitalWrite(LED6, HIGH);
  delay(500);
  }

void led3(){
  dode.right();
  allOff();
  digitalWrite(LED6, HIGH);
  delay(500);
  }

void led4(){
  dode.u_left();
  allOff();
  digitalWrite(LED6, HIGH);
  delay(500);
  }

void led5(){
  dode.u_right();
  allOff();
  digitalWrite(LED6, HIGH);
  delay(500);
  }

void led6(){
  for(int index = 0; index < 25; index++){
  if(index%5 == 0){
    led1();
    }else if(index%5 == 1){
      led2();
      }else if(index%5 == 2){
      led3();
      }else if(index%5 == 3){
      led4();
      }else if(index%5 == 4){
      led5();
      }
  }
  allOff();
  digitalWrite(LED6, HIGH);
  delay(1000);
  allOff();
  }

void led7(){
    
  }

void led8(){}

void led9(){}



void initialize(){
  // DodeFace(int pin, int t_cw1, int t_ccw1,int t_cw2, int t_ccw2, int t_cw3, int t_ccw3, int t_cw5, int t_ccw5, int pwm_stp)
  
  bottom->set(3,325,325,700,700,1000,1000,1500,1500,3500,3500,92);
  bottom_down->set(5,325,325,700,700,1000,1000,1500,1500,3500,3500,92);
  bottom_left->set(6,325,325,700,700,1000,900,1500,1500,3500,3500,92);
  bottom_right->set(9,325,325,700,700,1000,1200,1500,1500,3500,3500,93);
  bottom_u_left->set(10,325,325,700,700,1000,1000,1500,1500,3500,3500,92);
  bottom_u_right->set(11,325,325,700,700,1000,1000,1500,1500,3500,3500,92);

  top->set(0,325,325,700,700,1000,1000,1500,1500,3000,3000,336);
  top_down->set(0,325,325,700,700,1000,1000,1500,1500,3000,3000,336);
  top_left->set(0,325,325,700,700,1000,1000,1500,1500,3000,3000,337);

  
  top_right->set(0,325,325,700,700,1000,1000,1500,1500,3000,3000,336);
  top_u_left->set(0,325,325,700,700,1000,1000,1500,1500,3000,3000,336);
  top_u_right->set(0,325,325,700,700,1000,1000,1500,1500,3000,3000,336);

  setRelationships();
  dode = DodeFast(bottom);
   
  }


void setRelationships(){
  //Assign bottom Face Relationships  
  bottom->down = bottom_down;  
  bottom->left = bottom_left;
  bottom->right = bottom_right;
  bottom->u_left = bottom_u_left;
  bottom->u_right = bottom_u_right;

  //Assign buttom_down Face Relationships
  bottom_down->down = bottom;  
  bottom_down->left = bottom_right;
  bottom_down->right = bottom_left;
  bottom_down->u_left = top_left;
  bottom_down->u_right = top_down;

  //Assign buttom_left Face Relationships
  bottom_left->down = bottom;  
  bottom_left->left = bottom_down;
  bottom_left->right = bottom_u_left;
  bottom_left->u_left = top_down;
  bottom_left->u_right = top_right;
  
  //Assign buttom_right Face Relationships
  bottom_right->down = bottom;  
  bottom_right->left = bottom_u_right;
  bottom_right->right = bottom_down;
  bottom_right->u_left = top_u_left;
  bottom_right->u_right = top_left;
  
  //Assign buttom_u_left Face Relationships
  bottom_u_left->down = bottom;  
  bottom_u_left->left = bottom_left;
  bottom_u_left->right = bottom_u_right;
  bottom_u_left->u_left = top_right;
  bottom_u_left->u_right = top_u_right;
  
  //Assign buttom_u_right Face Relationships
  bottom_u_right->down = bottom;  
  bottom_u_right->left = bottom_u_left;
  bottom_u_right->right = bottom_right;
  bottom_u_right->u_left = top_u_right;
  bottom_u_right->u_right = top_u_left;

  //Assign top Face Relationships
  top->down = top_down;  
  top->left = top_left;
  top->right = top_right;
  top->u_left = top_down;
  top->u_right = top_u_right;

  //Assign top_down Face Relationships
  top_down->down = top;  
  top_down->left = top_right;
  top_down->right = top_left;
  top_down->u_left = bottom_left;
  top_down->u_right = bottom_down;

  //Assign top_left Face Relationships
  top_left->down = top;  
  top_left->left = top_down;
  top_left->right = top_u_left;
  top_left->u_left = bottom_down;
  top_left->u_right = bottom_right;

  //Assign top_right Face Relationships
  top_right->down = top;  
  top_right->left = top_u_right;
  top_right->right = top_down;
  top_right->u_left = bottom_u_left;
  top_right->u_right = bottom_left;

  //Assign top_u_left Face Relationships
  top_u_left->down = top;  
  top_u_left->left = top_left;
  top_u_left->right = top_u_right;
  top_u_left->u_left = bottom_right;
  top_u_left->u_right = bottom_u_right;

  //Assign top_u_right Face Relationships
  top_u_right->down = top;  
  top_u_right->left = top_u_left;
  top_u_right->right = top_right;
  top_u_right->u_left = bottom_u_right;
  top_u_right->u_right = bottom_u_left;
  
  }
