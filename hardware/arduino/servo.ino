void initServo(){
  servo.attach(SERVO_PIN);
}

void openAndCloseDoor(){
  int i = 90; 
  while(i>=0){
    currentMillis = millis();
    if((currentMillis - PREV_SERVO_MILLIS) >= INTERVAL){
      PREV_SERVO_MILLIS = currentMillis;
      servo.write(i);
      i--;
    }
  }
  while(i<90){
    currentMillis = millis();
    if((currentMillis - PREV_SERVO_MILLIS) >= INTERVAL){
      PREV_SERVO_MILLIS = currentMillis;
      servo.write(i);
      i++;
    }
  }
  Serial.println("init");
}

void closeDoor(){
  servo.write(90);
}

void openDoor(){
  servo.write(0);
}
