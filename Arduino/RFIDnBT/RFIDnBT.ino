#include <Servo.h>
#include <SPI.h>
#include <MFRC522.h>

int pinCafetera=7;
int pinEstereo=8;
int pinCochera=3;
int pinTV=6;
int pinLuzSala = 4;
int pinLuzCuarto = 5;
byte data;
bool access = false;

int pinBoton = 2; 
int pinRFID_is_read = A0;

const int ssPin = 10;
const int rstPin = 9;

// We define a MFRC522 class object
MFRC522 mfrc522(ssPin, rstPin);

Servo servoMotor;

void setup(){
    Serial.begin(9600);
    
    SPI.begin();
    mfrc522.PCD_Init();
    pinMode(pinCafetera, OUTPUT);
    pinMode(pinEstereo, OUTPUT);
    pinMode(pinCochera, OUTPUT);
    pinMode(pinTV, OUTPUT);
    pinMode(pinLuzSala, OUTPUT);
    pinMode(pinLuzCuarto, OUTPUT);
    pinMode(pinBoton, INPUT_PULLUP);
    pinMode(pinRFID_is_read, OUTPUT);
    servoMotor.attach(pinCochera);
    servoMotor.write(0);
}

void loop()
{
 
    if(!access)
    {
        // Look for a new card
        if(!mfrc522.PICC_IsNewCardPresent())
            return;
    
        // Select one of the cards
        if(!mfrc522.PICC_ReadCardSerial())
            return;
        
        // Show UID on serial monitor
        //Serial.print("UID tag: ");
        String content = "";
        byte letter;
    
        for(byte i = 0; i < mfrc522.uid.size; i++)
        {
            content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
            content.concat(String(mfrc522.uid.uidByte[i], HEX));
        }
        
        content.toUpperCase();
    
        // Change here the UID of the card/keychain that you want to give access
        if(content.substring(1) == "D0 BD 68 25")
        {  
            // We send a confirmation value to the user if the ID Card is correct
            Serial.write("1");
            access = true;
            digitalWrite(A0, HIGH);      
        }
      
        else
        {   
            Serial.write("0");
            access = false;
            digitalWrite(A0, LOW);
        }
    }
  
    if(access)
    {
        if(Serial.available()>0)
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
                  digitalWrite(pinCafetera,  LOW);
                  digitalWrite(pinEstereo, LOW);
                  digitalWrite(pinTV,LOW);
                  digitalWrite(pinLuzSala,LOW);
                  digitalWrite(pinLuzCuarto,LOW);
                  servoMotor.write(90);
                  break;
                case '7':
                  access = false;
                  login = false;
                  content = "";
            }
        }
    }
}
