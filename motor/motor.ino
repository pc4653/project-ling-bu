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
  int diff = 0;
  int spd = 50;
  if (Serial.available()){
    diff = Serial.parseInt();
    diff = diff + 641;
    Serial.println(diff);
    if(diff == 640){
     Serial.println("no face found");
     state = 7;
    }
    else if((diff < fwdRange) && (diff > -fwdRange)){
     Serial.println("straight ahead");
     state = 1;
     spd = 50;
      
    }
    else if(diff > fwdRange){
     Serial.println("turn right");      
     state = 3;
     spd = 0.0012*diff*diff + 48.737;
    }
    else if(diff < -fwdRange)
     Serial.println("turn left");    
     state = 2;
     spd = 0.0012*diff*diff + 48.737;
    
    }
  else {
    diff = 700;
    state = 7;
  }
  Serial.println(diff);
  Serial.println(state);
  drive(spd);
  delay(10);
}

void drive(int spd) {
  int constant_spd = 50;
    
  
  
  
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
      Motor1->setSpeed(constant_spd);  
      Motor2->setSpeed(spd);  
      Motor3->setSpeed(spd);  
      Motor4->setSpeed(constant_spd);   
      break;

    case S_FOR_RIGHT:
      Motor1->run(FORWARD);
      Motor2->run(FORWARD);
      Motor3->run(FORWARD);
      Motor4->run(FORWARD);
      Motor1->setSpeed(spd);  
      Motor2->setSpeed(constant_spd);  
      Motor3->setSpeed(constant_spd);  
      Motor4->setSpeed(spd);   
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
