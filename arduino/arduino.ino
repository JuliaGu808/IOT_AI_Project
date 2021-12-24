#include "includes.h"
#include "config.h"

void setup() {
  initSerial();
  initServo();
  initButton();
}

void loop() {
  checkBtnState();
  if(Serial.available()>0){
    String message=Serial.readStringUntil('\n');
    if(message=="open"){
      openAndCloseDoor();
    }
  }

  
  
 // closeDoor();
//  delay(1000);
//  openDoor();
//  delay(3000);
  
 // openAndCloseDoor();
}
