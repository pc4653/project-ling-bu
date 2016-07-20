#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

//definte states
#define S_FOR_STRAIGHT  (1)
#define S_FOR_LEFT      (2)
#define S_FOR_RIGHT     (3)
#define S_BAC_STRAIGHT  (4)
#define S_BAC_LEFT      (5)
#define S_BAC_RIGHT     (6)
#define S_STOP          (7)


Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *Motor1 = AFMS.getMotor(1);
Adafruit_DCMotor *Motor2 = AFMS.getMotor(2);
Adafruit_DCMotor *Motor3 = AFMS.getMotor(3);
Adafruit_DCMotor *Motor4 = AFMS.getMotor(4);
const int fwdRange = 32;
int state = 7;


void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Adafruit Motorshield v2 - DC Motor test!");

  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
//  // Set the speed to start, from 0 (off) to 255 (max speed)
//  myMotor->setSpeed(150);
//  myMotor->run(FORWARD);
//  // turn on motor
//  myMotor->run(RELEASE);
}

void loop() {

  if (Serial.available()){
    state = Serial.parseInt();
    
    }
  Serial.println(state);
  drive();
  delay(1000);
}

void drive() {
  int spd = 50;
  
  switch(state) {
    case S_FOR_STRAIGHT:
      Motor1->run(FORWARD);
      Motor2->run(FORWARD);
      Motor3->run(FORWARD);
      Motor4->run(FORWARD);
      Motor1->setSpeed(spd);  
      Motor2->setSpeed(spd);  
      Motor3->setSpeed(spd);  
      Motor4->setSpeed(spd);   
      break;
      
    case S_FOR_LEFT:
      Motor1->run(FORWARD);
      Motor2->run(FORWARD);
      Motor3->run(FORWARD);
      Motor4->run(FORWARD);
      Motor1->setSpeed(50);  
      Motor2->setSpeed(200);  
      Motor3->setSpeed(200);  
      Motor4->setSpeed(50);   
      break;

    case S_FOR_RIGHT:
      Motor1->run(FORWARD);
      Motor2->run(FORWARD);
      Motor3->run(FORWARD);
      Motor4->run(FORWARD);
      Motor1->setSpeed(200);  
      Motor2->setSpeed(50);  
      Motor3->setSpeed(50);  
      Motor4->setSpeed(200);   
      break;

    case S_BAC_STRAIGHT:
      Motor1->run(BACKWARD);
      Motor2->run(BACKWARD);
      Motor3->run(BACKWARD);
      Motor4->run(BACKWARD);
      Motor1->setSpeed(75);  
      Motor2->setSpeed(75);  
      Motor3->setSpeed(75);  
      Motor4->setSpeed(75);   
      break;
      
    case S_BAC_LEFT:
      Motor1->run(FORWARD);
      Motor2->run(BACKWARD);
      Motor3->run(BACKWARD);
      Motor4->run(FORWARD);
      Motor1->setSpeed(75);  
      Motor2->setSpeed(75);  
      Motor3->setSpeed(75);  
      Motor4->setSpeed(75);   
      break;

    case S_BAC_RIGHT:
      Motor1->run(BACKWARD);
      Motor2->run(FORWARD);
      Motor3->run(FORWARD);
      Motor4->run(BACKWARD);
      Motor1->setSpeed(75);  
      Motor2->setSpeed(75);  
      Motor3->setSpeed(75);  
      Motor4->setSpeed(75);   
      break;
    case S_STOP:
      Motor1->run(RELEASE);
      Motor2->run(RELEASE);
      Motor3->run(RELEASE);
      Motor4->run(RELEASE); 
  }
}
