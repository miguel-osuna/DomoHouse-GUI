#include <Servo.h>

int pinCafetera = 7;
int pinEstereo = 8;
int pinCochera = 3;
int pinTV = 6;
int pinLuzSala = 4;
int pinLuzCuarto = 5;
byte data;
Servo servoMotor;

void setup(){
  Serial.begin(9600);
  servoMotor.attach(pinCochera);
  
  pinMode(pinCafetera, OUTPUT);
  pinMode(pinEstereo, OUTPUT);
  pinMode(pinCochera, OUTPUT);
  pinMode(pinTV, OUTPUT);
  pinMode(pinLuzSala, OUTPUT);
  pinMode(pinLuzCuarto, OUTPUT);

  digitalWrite(pinCafetera, LOW);
  digitalWrite(pinEstereo, LOW);
  digitalWrite(pinCochera, LOW);
  digitalWrite(pinTV, LOW);
  digitalWrite(pinLuzSala, LOW);
  digitalWrite(pinLuzCuarto, LOW);
}

void loop(){
 
  if(Serial.available())
  {   
    data = Serial.read();
    switch(data)
    {
      case '0':
        servoMotor.write(0);
        break;
        
      case '1':
        digitalWrite(pinCafetera,HIGH);
        break;
        
      case '2':
        digitalWrite(pinEstereo, HIGH);
        break;
        
      case '3':
        digitalWrite(pinTV,HIGH);
        break;
        
      case '4':
        digitalWrite(pinLuzSala,HIGH);
        break;
        
      case '5':
        digitalWrite(pinLuzCuarto,HIGH);
        break;
        
      case '6':
        digitalWrite(pinCochera, LOW);
        digitalWrite(pinCafetera,  LOW);
        digitalWrite(pinEstereo, LOW);
        digitalWrite(pinTV,LOW);
        digitalWrite(pinLuzSala,LOW);
        digitalWrite(pinLuzCuarto,LOW);
        servoMotor.write(90);
    }
  }
}
