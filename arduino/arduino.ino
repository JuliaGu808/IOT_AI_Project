#include "includes.h"
#include "config.h"

void setup() {
  initSerial();
  initServo();
  initButton();
}

void loop() {
  checkBtnState();

  
  
 // closeDoor();
//  delay(1000);
//  openDoor();
//  delay(3000);
  
 // openAndCloseDoor();
}
