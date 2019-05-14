#include <Servo.h>

int pinCafetera=7;
int pinEstereo=8;
int pinCochera=9;
int pinTV=10;
int pinLuzSala = 11;
int pinLuzCuarto = 12;

int pinBoton = 2; 
byte data;

Servo servoMotor;

void setup(){
  Serial.begin(9600);
  
  pinMode(pinCafetera, OUTPUT);
  pinMode(pinEstereo, OUTPUT);
  pinMode(pinCochera, OUTPUT);
  pinMode(pinTV, OUTPUT);
  pinMode(pinLuzSala, OUTPUT);
  pinMode(pinLuzCuarto, OUTPUT);
  pinMode(pinBoton, INPUT_PULLUP);
  
  servoMotor.attach(pinCochera);
  servoMotor.write(0);
}

void loop(){
  
  if(digitalRead(pinBoton)==LOW)
  {
    for(int i = 0; i <= 180;i++)
      {
        servoMotor.write(i);
        delay(15);
      }
  
  if(Serial.available()>0)//Si llega un dato
  {   
    data = Serial.read();//Leelo
    switch(data)
    {
      case '0':
      
        //digitalWrite(pinCochera, HIGH);
        break;
      case '1':
      for(int i = 180; i >= 1;i--)
      {
        servoMotor.write(i);
        delay(15);
      }
      digitalWrite()

        break;
      case '2':
        digitalWrite(pinCafetera,HIGH);
        break;
      case '3':
        digitalWrite(pinCafetera,LOW);
        break;
      case '4':
        digitalWrite(pinEstereo, HIGH);
        break;
      case '5':
        digitalWrite(pinEstereo, LOW);
        break;
      case '6':
        digitalWrite(pinTV,HIGH);
        break;
      case '7':
        digitalWrite(pinTV, LOW);
        break; 
      case '8':
        digitalWrite(pinLuzSala,HIGH);
        break;
      case '9':
        digitalWrite(pinLuzSala, LOW);
        break;
      case 'A':
        digitalWrite(pinLuzCuarto,HIGH);
        break;
      case 'B':
        digitalWrite(pinLuzCuarto,LOW);
        break;
        
    }

    
    
  }
 }
}
