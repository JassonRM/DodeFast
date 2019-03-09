#define LED1 2
#define LED2 3

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(LED1,OUTPUT);
pinMode(LED2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  String data;
  if(Serial.available()>0){
      data = Serial.readString();
      Serial.println("Recibido: '" + data + "'");
      }
      if(data == "Amarillo"){
        Serial.println("Encendiendo amarillo");
        led1();
        }
      if(data == "Verde"){
        Serial.println("Encendiendo verde");
        led2();
        }
}

void led1(){
  digitalWrite(LED2, LOW);
  digitalWrite(LED1, HIGH);
  delay(500);
  }

void led2(){
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, HIGH);
  delay(500);
  }
