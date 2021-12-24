#include <Servo.h>

#define SERVO_PIN 12

Servo servo;

void setup() {
  servo.attach(SERVO_PIN);
}

void loop() {
  for(int i = 0; i < 180; i++){
    servo.write(i);
    delay(10);
  }
  for(int i = 180; i >= 0; i--){
    servo.write(i);
    delay(10);
  }
}
